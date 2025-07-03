#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import json
import os

# ---------------
# CONFIGURATION

fileDir = os.path.realpath(__file__)

dataDirectory = os.path.join(fileDir, "../data")
gabctkDirectory = os.path.join(fileDir, "../../gabctk")
gabctkScript = "gabctk.py"
outputDirectoryLy = ""
outputDirectoryMidi = ""
outputDirectoryXml = ""

print(f"------ CONVERTING GABC TO LY -------")
print(f"fileDir: {fileDir}")
print(f"dataDirectory: {dataDirectory}")
print(f"gabctkDirectory: {gabctkDirectory}")
print(f"------------------------------------\n")

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

print(f"------ USING GABCTK -------")
print(f"inFilePath: {inFilePath}")
print(f"outFilePath: {outFilePath}")
print(f"cmdString: {cmdString}")
print(f"---------------------------\n")

try:
    retcode = subprocess.call(cmdString, shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)
