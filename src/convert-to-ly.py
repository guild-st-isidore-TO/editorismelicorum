#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import json

# ---------------
# CONFIGURATION

dataDirectory = "data/"
gabctkDirectory = ""
outputDirectoryLy = ""
outputDirectoryMidi = ""
outputDirectoryXml = ""

with open("./config.json", "r") as file:
    cfgData = json.load(file)
    gabctkDirectory = cfgData["gabctkDirectory"]
    outputDirectoryLy = cfgData["outputDirectoryLy"]
    outputDirectoryMidi = cfgData["outputDirectoryMidi"]
    outputDirectoryXml = cfgData["outputDirectoryXml"]

# ------------
# DATA FILES

gabcDataFiles = [
    "data/an--regina_caeli--simplex.gabc",
    "data/hy--tantum_ergo--vatican.gabc",
    "data/of--ave_maria--simplex.gabc",
]

# --------------
# USING GABCTK

inFilePath = gabcDataFiles[0]
outFilePath = f"{outputDirectoryLy}/test.ly"
cmdString = f"gabctk.py -i {inFilePath} -l {outFilePath} -v"

try:
    retcode = subprocess.call(cmdString, shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)
