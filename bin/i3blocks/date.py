#!/usr/bin/env python
import json
import subprocess

from colours import *

CALENDAR_SYMBOL = '📅'

# Shell out to get the date
day = subprocess.run(['date', '+%a'],
        capture_output=True).stdout.decode('utf-8').strip()

result = subprocess.run(['date', '+%d-%m-%Y'], capture_output=True)
date = result.stdout.decode('utf-8').strip()

markup = f' {CALENDAR_SYMBOL} <span foreground="{WHITE}"><b>{day}</b> {date} ' \
    + '</span>'

print(json.dumps({
    'full_text': markup
}, ensure_ascii=False))
