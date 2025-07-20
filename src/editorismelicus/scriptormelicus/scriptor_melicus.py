#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Engraver of Music gets all the packaged info written out and ready for publishing.

import sys
import subprocess
import json
import os
from pathlib import Path

from .. import ed_melicus_utils

# ---------------
# CONFIGURATION

fileDir = os.path.dirname(os.path.realpath(__file__))

dataDirectory = os.path.join(fileDir, "../data")
gabctkScript = "gabctk.py"

gabctkDirectory = ""
outputDirectoryLy = ""

cfg_data = {
    "dataDirectory": dataDirectory,
    "gabctkDirectory": gabctkDirectory,
}
ed_melicus_utils.print_frame("PROCESSING CONVERTED LILYPOND FILE", cfg_data)

with open(f"{dataDirectory}/configs.json", "r") as file:
    cfgData = json.load(file)
    gabctkDirectory = os.path.join(fileDir, cfgData["gabctkDirectory"])
    outputDirectoryLy = os.path.join(fileDir, cfgData["outputDirectoryLy"])

cfg_data = {
    "gabctkDirectory": gabctkDirectory,
    "outputDirectoryLy": outputDirectoryLy,
}
ed_melicus_utils.print_frame("CONFIGURATION", cfg_data)
