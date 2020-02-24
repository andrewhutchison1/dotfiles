#!/usr/bin/env python
import json
import subprocess

from colours import *

CLOCK_SYMBOL = '🕐'

# Shell out to get the time
result = subprocess.run(['date', '+%H:%M'], capture_output=True)
time = result.stdout.decode('utf-8').strip()

markup = f' {CLOCK_SYMBOL} <b><span foreground="{WHITE}">{time} </span></b>'

print(json.dumps({
    'full_text': markup
}, ensure_ascii=False))
