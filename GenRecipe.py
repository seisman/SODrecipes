#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import argparse

parser = argparse.ArgumentParser(description='Paste event, network and waveform arms into one xml.')

parser.add_argument('-e', action="store", dest="eventArm", help="specify eventArm")
parser.add_argument('-n', action="store", dest="networkArm", help="specify networkArm")
parser.add_argument('-w', action="store", dest="waveformArm", help="specify waveformArm")
args = parser.parse_args()

print('<?xml version="1.0"?>')
print('<sod>')

for arm in [args.eventArm, args.networkArm, args.waveformArm]:    
    if arm:
        with open(arm, "r") as f:
            lines = f.read()
            print(lines)

print('</sod>')