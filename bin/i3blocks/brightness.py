#!/usr/bin/env python
import json
import subprocess
import sys
import collections
import re

from colours import *

SYMBOL = '☀'

def get_brightness_data():
    result = subprocess.run(['xbacklight', '-get'], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    return int(round(float(output)))

def main(argv):
    brightness = get_brightness_data()
    full_text = f' {SYMBOL} <span foreground="{WHITE}">{brightness}%</span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
