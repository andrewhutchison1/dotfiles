#!/usr/bin/env python
import json
import subprocess
import sys
import collections
import re

from colours import *

VolumeInfo = collections.namedtuple('VolumeInfo',
        ['muted', 'volume'])

UNMUTED_SYMBOL = '🔊'
MUTED_SYMBOL = '🔇'

def get_volume_data():
    result = subprocess.run(['amixer', 'sget', 'Master'], capture_output=True)
    output = result.stdout.decode('utf-8')
    vol_muted = re.search('Mono: Playback \d+ \[(\d+)%\] \[.+\] \[([a-z]+)\]',
            output)

    vol = int(vol_muted.group(1))
    muted = vol_muted.group(2) == 'off'
    return VolumeInfo(muted, vol)

def main(argv):
    muted, vol = get_volume_data()
    colour = RED if muted else WHITE
    symbol = MUTED_SYMBOL if muted else UNMUTED_SYMBOL
    text = '<b>MUTED</b>' if muted else f'{vol}%'

    full_text = f' {symbol} <span foreground="{colour}">{text}</span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
