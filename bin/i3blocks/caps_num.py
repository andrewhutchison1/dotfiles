#!/usr/bin/env python
import json
import subprocess
import sys
import collections
import re

from colours import *

KeyInfo = collections.namedtuple('KeyInfo', ['caps', 'num'])

def get_key_data():
    result = subprocess.run(['xset', '-q'], capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    result = re.search('Caps Lock:\s+([a-z]+).+Num Lock:\s+([a-z]+)', output)

    caps = result.group(1).strip() == 'on'
    num = result.group(2).strip() == 'on'
    return KeyInfo(caps, num)

def main(argv):
    caps, num = get_key_data()

    if caps and num:
        text = "CAPS NUM"
    elif caps:
        text = "CAPS"
    elif num:
        text = "NUM"
    else:
        text = ''

    full_text = f' <span foreground="{DARK_GRAY}"><b>{text}</b></span> '

    print(json.dumps({
        'full_text': full_text
    }, ensure_ascii=False))

if __name__ == '__main__':
    main(sys.argv)
