#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Reader of Music is in charge of re-copying music from outside.

import sys
import subprocess
import os
from pathlib import Path

from ed_melicus_utils import print_frame, get_cfg_data

# ---------------
# CONFIGURATION

fileDir = os.path.dirname(os.path.realpath(__file__))
cfg_data = get_cfg_data()

Path(cfg_data["output_dir_ly_data"]).mkdir(parents=True, exist_ok=True)


def lege_tabulae_gabc(gabc_data_files):
    """Reads a GABC file, and..."""
    for gabcDataFile in gabc_data_files:

        inFilePath = gabcDataFile
        inFileName = os.path.basename(inFilePath)
        outFileName = inFileName.replace(".gabc", "")
        outFilePath = f"{cfg_data["output_dir_ly_data"]}/{outFileName}.ly"
        cmdString = f"{cfg_data["gabctk_dir"]}/{cfg_data['gabctk_script_fname']} -i {inFilePath} -l {outFilePath} -v"

        print(gabc_data_files)
        print(cmdString)
        print_frame("USING GABCTK", cfg_data)

        try:
            retcode = subprocess.call(cmdString, shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child returned", retcode, file=sys.stderr)
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)


def mark_conv_gabc_line(conv_ly_line, action, data):
    """Use the given action and data to do something with the LY line"""
    return 0


def analyze_conv_gabc_line(conv_ly_line):
    """Checks a line of converted LY code (from gabctk) for certain features. Decides the appropriate action based on string patterns."""
    subject_line = conv_ly_line.strip()

    # ---------------
    #  DECLARATIONS

    if "\\version" in subject_line:
        return "version"
    if "\\midi{}" in subject_line:
        return "midi"
    elif "\\header" in subject_line:
        return "header"
    elif "\\paper" in subject_line:
        return "paper"

    # ---------------
    #  VARIABLES

    elif "MusiqueTheme =" in subject_line:
        return "musiquetheme"
    elif "Paroles =" in subject_line:
        return "paroles"

    # ---------------------------
    #  SCORE CREATION

    elif "\\score" in subject_line:
        return "score"
    elif "  <<" in subject_line:
        return "staffgroup"
    elif "\\new Staff <<" in subject_line:
        return "staff"
    elif "\\new Voice" in subject_line:
        return "voice"
    elif "\\new Lyrics" in subject_line:
        return "lyrics"
    elif "\\layout" in subject_line:
        return "layout"
    elif "\\context" in subject_line:
        return "context"
    elif "%" in subject_line:
        return "comment"
    elif "}" == subject_line:
        return "end_bracket"
    elif ">>" in subject_line:
        return "end_dbl_ang_bracket"
    else:
        return None


def copy_conv_gabc_vars(conv_ly_filepath, out_ly_path):
    """Reads and copies a file of converted LY code (from gabctk)"""
    ly_script_stack = []
    conv_filename = os.path.basename(conv_ly_filepath).replace(".ly", "")
    conv_filename = conv_filename.replace("-", " ")
    conv_filename = conv_filename.title().replace(" ", "")
    music_name = f"Music{conv_filename}"
    lyrics_name = f"Lyrics{conv_filename}"

    bracket_delim_blocks = [
        "header",
        "paper",
        "musiquetheme",
        "paroles",
        "score",
        "lyrics",
        "layout",
        "voice",
        "context",
    ]

    dbl_ang_bracket_delim_blocks = ["staffgroup", "staff"]

    with open(conv_ly_filepath) as f:
        with open(out_ly_path, "w") as wr:
            for ly_line in f:
                script_evt_type = analyze_conv_gabc_line(ly_line)
                is_valid_copy = False
                print(
                    "- event: "
                    + str(script_evt_type)
                    + "\n         stack: "
                    + str(ly_script_stack)
                )
                if script_evt_type is not None:
                    if (
                        script_evt_type in bracket_delim_blocks
                        or script_evt_type in dbl_ang_bracket_delim_blocks
                    ):
                        print("         adding to stack: " + script_evt_type)
                        ly_script_stack.append(script_evt_type)

                    if (
                        "musiquetheme" in ly_script_stack
                        or "paroles" in ly_script_stack
                    ):
                        is_valid_copy = True

                    if (
                        script_evt_type == "end_bracket"
                        and ly_script_stack[-1] in bracket_delim_blocks
                    ):
                        print(
                            "         found end of block. Removing from stack: "
                            + ly_script_stack[-1]
                        )
                        ly_script_stack.remove(ly_script_stack[-1])
                    elif (
                        script_evt_type == "end_dbl_ang_bracket"
                        and ly_script_stack[-1] in dbl_ang_bracket_delim_blocks
                    ):
                        print(
                            "         found end of double angle block. Removing from stack: "
                            + ly_script_stack[-1]
                        )
                        ly_script_stack.remove(ly_script_stack[-1])

                    if is_valid_copy:
                        valid_line = ly_line
                        if "MusiqueTheme =" in valid_line:
                            valid_line = valid_line.replace("MusiqueTheme", music_name)
                        if "Paroles =" in valid_line:
                            wr.write("\n")
                            valid_line = valid_line.replace("Paroles", lyrics_name)
                        wr.write(valid_line)

                else:
                    # "Regular degular" text lines

                    if (
                        "musiquetheme" in ly_script_stack
                        or "paroles" in ly_script_stack
                    ):
                        ## Only writing variables data, so when 'musiquetheme'
                        ## and 'paroles' are on the stack
                        wr.write(ly_line)
    return 0
