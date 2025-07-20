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

docDirectory = os.path.join(fileDir, "../../document")
cfgDirectory = fileDir

outputDirectoryLy = ""
outputDirectoryPdf = ""

print(f"\n\n====== BUILDING DOCUMENT (PREVIEW) ======")
print(f"fileDir: {fileDir}")
print(f"docDirectory: {docDirectory}")
print(f"------------------------------------\n")

with open(f"{cfgDirectory}/config.json", "r") as file:
    cfgData = json.load(file)
    outputDirectoryLy = os.path.join(fileDir, cfgData["outputDirectoryLy"])
    outputDirectoryPdf = os.path.join(fileDir, cfgData["outputDirectoryPdf"])

print(f"------ CONFIGURATION -------")
print(f"outputDirectoryLy: {outputDirectoryLy}")
print(f"outputDirectoryPdf: {outputDirectoryPdf}")
print(f"----------------------------\n")

Path(outputDirectoryLy).mkdir(parents=True, exist_ok=True)
Path(outputDirectoryPdf).mkdir(parents=True, exist_ok=True)

# --------------
# USING LILYPOND

inFilePath = f"{docDirectory}/vol-1-hello-world.ly"
outFilePath = f"{outputDirectoryPdf}"
cmdString = f"lilypond -l VERBOSE -o {outFilePath} {inFilePath}"


def praedica_min():

    print(f"------ USING LILYPOND -------")
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
