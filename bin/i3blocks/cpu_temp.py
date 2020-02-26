#!/usr/bin/env python
import json
import subprocess
import sys
import collections
import re

from colours import *

VolumeInfo = collections.namedtuple('VolumeInfo',
        ['muted', 'volume'])

TEMP_SYMBOL = '🌡'

def get_temp_data():
    result = subprocess.run(['sensors'], capture_output=True)
    output = result.stdout.decode('utf-8')

    ts = [float(s) for s in re.findall('Core \d:\s+((?:\+|-)\d+.\d+)', output)]
    avg = sum(ts) / len(ts)
    return round(avg, 1)

def get_colour(temp):
    if temp <= 25:
        return BLUE
    elif temp <= 50:
        return GREEN
    elif temp <= 75:
        return YELLOW
    else:
        return RED

def main(argv):
    temp = get_temp_data()
    colour = get_colour(temp)
    text = f'<b>{temp}</b>°C'
    full_text = f' {TEMP_SYMBOL} <span foreground="{colour}">{text}</span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
