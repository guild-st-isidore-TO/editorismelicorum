#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import json
import os
from pathlib import Path

# ---------------
# CONFIGURATION

fileDir = os.path.dirname(os.path.realpath(__file__))

dataDirectory = os.path.join(fileDir, "../data")
cfgDirectory = fileDir
gabctkScript = "gabctk.py"

gabctkDirectory = ""
outputDirectoryLy = ""
outputDirectoryMidi = ""
outputDirectoryXml = ""

print(f"\n\n====== CONVERTING GABC TO LY ======")
print(f"fileDir: {fileDir}")
print(f"dataDirectory: {dataDirectory}")
print(f"gabctkDirectory: {gabctkDirectory}")
print(f"------------------------------------\n")

with open(f"{cfgDirectory}/config.json", "r") as file:
    cfgData = json.load(file)
    gabctkDirectory = os.path.join(fileDir, cfgData["gabctkDirectory"])
    outputDirectoryLy = os.path.join(fileDir, cfgData["outputDirectoryLy"])
    outputDirectoryMidi = os.path.join(fileDir, cfgData["outputDirectoryMidi"])
    outputDirectoryXml = os.path.join(fileDir, cfgData["outputDirectoryXml"])

print(f"------ CONFIGURATION -------")
print(f"gabctkDirectory: {gabctkDirectory}")
print(f"outputDirectoryLy: {outputDirectoryLy}")
print(f"outputDirectoryMidi: {outputDirectoryMidi}")
print(f"outputDirectoryXml: {outputDirectoryXml}")
print(f"----------------------------\n")

Path(outputDirectoryLy).mkdir(parents=True, exist_ok=True)
Path(outputDirectoryMidi).mkdir(parents=True, exist_ok=True)
Path(outputDirectoryXml).mkdir(parents=True, exist_ok=True)

# ------------
# DATA FILES

gabcDataFiles = [
    "data/01_an--regina_caeli--simplex.gabc",
    "data/02_hy--tantum_ergo--vatican.gabc",
    "data/03_of--ave_maria--simplex.gabc",
]

# --------------
# USING GABCTK

for gabcDataFile in gabcDataFiles:

    inFilePath = gabcDataFile
    inFileName = os.path.basename(inFilePath)
    outFileName = inFileName.replace(".gabc", "")
    outFilePath = f"{outputDirectoryLy}/{outFileName}.ly"
    cmdString = f"{gabctkDirectory}/{gabctkScript} -i {inFilePath} -l {outFilePath} -v"

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
