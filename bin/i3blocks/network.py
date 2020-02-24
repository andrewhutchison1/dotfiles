#!/usr/bin/env python
import collections
import json
import subprocess
import re
import sys

from colours import *

NetworkInfo = collections.namedtuple('NetworkInfo',
        ['connected', 'essid', 'quality'])

NETWORK_SYMBOL = '📶'
INTERFACE = 'wlp59s0'

def dBm_to_quality(dBm):
    if dBm <= -100:
        quality = 0
    elif dBm >= -50:
        quality = 100
    else:
        quality = 2 * (dBm + 100)

    return quality

def get_network_data():
    result = subprocess.run(['iwconfig', INTERFACE], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    
    ssid = re.search('ESSID:"?([a-zA-Z0-9_/-]+)"?', output).group(1).strip()
    connected = True if ssid != 'off/any' else False

    if not connected:
        return NetworkInfo(False, None, None)

    dBm = int(re.search('Signal level=(-?\d+)', output).group(1).strip())
    quality = dBm_to_quality(dBm)
    return NetworkInfo(True, ssid, quality)

def get_colour(connected, quality):
    if not connected:
        return RED

    if quality <= 50:
        return DARK_YELLOW
    elif quality <= 75:
        return YELLOW
    else:
        return GREEN

def main(argv):
    connected, essid, quality = get_network_data()
    colour = get_colour(connected, quality)
    full_text = f' {NETWORK_SYMBOL}'

    if not connected:
        full_text = full_text + f'<span foreground="{colour}"> ' + \
                '<b>Disconnected</b></span> '
    else:
        full_text = full_text + f'<span foreground="{colour}"> ' + \
                f'<b>{essid}</b> ({quality}%)</span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
