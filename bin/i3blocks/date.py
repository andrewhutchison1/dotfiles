#!/usr/bin/env python
import collections
import json
import subprocess
import sys

from colours import *

CALENDAR_SYMBOL = '📅'

DateInfo = collections.namedtuple('DateInfo', ['day', 'date', 'cw'])

def get_date_info():
    result = subprocess.run(['date', '+%a %d/%m/%Y %V'], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    return DateInfo(*output.split())

def main(argv):
    date_info = get_date_info()

    markup = f' {CALENDAR_SYMBOL} '
    markup += f'<span foreground="{WHITE}">'
    markup += f'<b>{date_info.day}</b> {date_info.date} (CW {date_info.cw}) '
    markup += '</span>'

    print(json.dumps({
        'full_text': markup
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
