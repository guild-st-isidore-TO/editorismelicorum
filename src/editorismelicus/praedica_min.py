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

repo_dir = get_repo_dir()

cfg_data = {
    "doc_dir": os.path.join(repo_dir, "document"),
    "data_dir": os.path.join(repo_dir, "data"),
}

with open(f"{cfg_data['data_dir']}/configs.json", "r") as file:
    cfg_json = json.load(file)
    cfg_data["output_dir_ly"] = os.path.join(
        repo_dir, cfg_json["paths"]["outputDirectoryLy"]
    )
    cfg_data["output_dir_pdf"] = os.path.join(
        repo_dir, cfg_json["paths"]["outputDirectoryPdf"]
    )

Path(cfg_data["output_dir_ly"]).mkdir(parents=True, exist_ok=True)
Path(cfg_data["output_dir_pdf"]).mkdir(parents=True, exist_ok=True)

# --------------
# USING LILYPOND

cfg_data["in_file_path"] = f"{cfg_data['doc_dir']}/vol-1-hello-world.ly"
cfg_data["out_file_path"] = f"{cfg_data['output_dir_pdf']}"
cfg_data["cmd_string"] = (
    f"lilypond -l VERBOSE -o {cfg_data['out_file_path']} {cfg_data['in_file_path']}"
)


def praedica_min():
    print_frame("USING LILYPOND", cfg_data)

    try:
        retcode = subprocess.call(cfg_data["cmd_string"], shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=sys.stderr)
        else:
            print("Child returned", retcode, file=sys.stderr)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
