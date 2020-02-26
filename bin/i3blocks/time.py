#!/usr/bin/env python
import json
import subprocess
import sys
import collections

from colours import *

TimeInfo = collections.namedtuple('TimeInfo', ['time', 'timezone'])

CLOCK_SYMBOL = '🕐'



def get_time_data():
    # Shell out to get the time
    result = subprocess.run(['date', '+%H:%M %Z'], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    return TimeInfo(*output.split())

def main(argv):
    time_info = get_time_data()

    markup = f' {CLOCK_SYMBOL} '
    markup += f'<span foreground="{WHITE}">'
    markup += f'<b>{time_info.time}</b> {time_info.timezone} '
    markup += '</span>'

    print(json.dumps({
        'full_text': markup
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)

