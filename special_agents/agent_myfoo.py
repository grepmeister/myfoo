#!/usr/bin/env python3

import sys
import json

# pip3 install pprintpp
from pprintpp import pprint as pp


def write_section(data):
    print("<<<local>>>")
    for item in data:
        print("0 %s - nothing" % item.get("url"))


def main():
    try:
        data = json.loads(sys.stdin.read())
    except:
        print("could not parse json from stdin")
    write_section(data)
    # print( list(sys.argv))
