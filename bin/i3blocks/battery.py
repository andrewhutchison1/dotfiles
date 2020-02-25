#!/usr/bin/env python
import json
import subprocess
import sys
import collections

from colours import *

PowerInfo = collections.namedtuple('PowerInfo',
        ['state', 'charge', 'h', 'm', 's'])

BATTERY_SYMBOL = '🗲'

def get_power_data():
    result = subprocess.run(['acpi', '-b'], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    split = output.split()
    state = split[2].strip()[:-1]

    if state == 'Full':
        return PowerInfo(state, None, None, None, None)

    charge, time = output.split()[3:5]
    h, m, s = time.split(':')
    return PowerInfo(state, int(charge[:-2]), int(h), int(m), int(s))

def get_colour(charge):
    if charge <= 5:
        return RED
    elif charge <= 15:
        return DARK_YELLOW
    elif charge <= 30:
        return YELLOW
    else:
        return GREEN

def main(argv):
    state, charge, h, m, _ = get_power_data()

    if state == 'Full':
        colour = GREEN
        full_text = f' {BATTERY_SYMBOL} <span foreground="{colour}">' + \
                '<b>100%</b></span> '
    else:
        colour = get_colour(charge)
        h = f'{h} hr' if h else ''
        m = f'{m} min' if m else ''
        sp = ' ' if (h or not m) else ''
        full_text = f' {BATTERY_SYMBOL}' + \
                f' <span foreground="{colour}"><b>{charge}%</b> {state}' + \
                f' ({h}{sp}{m})</span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
