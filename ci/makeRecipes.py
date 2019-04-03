#!/usr/bin/env python
import os
import glob

eventArm = glob.glob("../eventArm/*.xml")
networkArm = glob.glob("../networkArm/*.xml")
waveformArm = glob.glob("../waveformArm/*.xml")


def buildRecipe(eventArm=None, networkArm=None, waveformArm=None, recipe=None):
    with open(recipe, "w") as frcp:
        frcp.write('<?xml version="1.0"?>\n')

        frcp.write('<sod>\n\n')
        for arm in (eventArm, networkArm, waveformArm):
            if arm:
                with open(arm, "r") as farm:
                    for line in farm:
                        frcp.write(line)
                frcp.write('\n')
        frcp.write('</sod>\n')

for arm in eventArm:
    buildRecipe(eventArm=arm, recipe=os.path.basename(arm))

for arm in networkArm:
    buildRecipe(networkArm=arm, recipe=os.path.basename(arm))

for arm in waveformArm:
    buildRecipe(eventArm=eventArm[0], networkArm=networkArm[0], waveformArm=arm, recipe=os.path.basename(arm))
