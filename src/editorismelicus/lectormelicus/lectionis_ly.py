#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import json
import os
from pathlib import Path

from ed_melicus_utils import get_repo_dir, print_frame

# ---------------
# CONFIGURATION

fileDir = os.path.dirname(os.path.realpath(__file__))

gabctkScript = "gabctk.py"

repo_dir = get_repo_dir()

cfg_data = {
    "doc_dir": os.path.join(repo_dir, "document"),
    "data_dir": os.path.join(repo_dir, "data"),
}

with open(f"{cfg_data['data_dir']}/configs.json", "r") as file:
    cfg_json = json.load(file)
    cfg_data["gabctk_dir"] = os.path.join(
        repo_dir, cfg_json["paths"]["gabctkDirectory"]
    )
    cfg_data["output_dir_ly_data"] = os.path.join(
        repo_dir, cfg_json["paths"]["outputDirectoryLyData"]
    )

Path(cfg_data["output_dir_ly_data"]).mkdir(parents=True, exist_ok=True)

# ------------
# DATA FILES

gabcDataFiles = [
    "data/01_an--regina_caeli--simplex.gabc",
    "data/02_hy--tantum_ergo--vatican.gabc",
    "data/03_of--ave_maria--simplex.gabc",
]


def lege_tabula_gabc():

    # --------------
    # USING GABCTK

    for gabcDataFile in gabcDataFiles:

        inFilePath = gabcDataFile
        inFileName = os.path.basename(inFilePath)
        outFileName = inFileName.replace(".gabc", "")
        outFilePath = f"{cfg_data["output_dir_ly_data"]}/{outFileName}.ly"
        cmdString = f"{cfg_data["gabctk_dir"]}/{gabctkScript} -i {inFilePath} -l {outFilePath} -v"

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
