#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Reader of Music is in charge of copying and editing music from outside the shop.

import sys
import subprocess
import os
from pathlib import Path

from ed_melicorum_utils import print_frame, get_cfg_data

# ---------------
# CONFIGURATION

fileDir = os.path.dirname(os.path.realpath(__file__))
cfg_data = get_cfg_data()

Path(cfg_data["output_dir_ly_data"]).mkdir(parents=True, exist_ok=True)


def get_gabc_metadata(gabc_data_file):
    source_abbrevs = {
        "Liber antiphonarius, 1960": "L.Ant '60",
        "The Liber Usualis, 1961": "L.Usu '61",
        "Chants of the Church, 1956": "Ch.otC '56",
        "Graduale Romanum, 1908": "G.Rom '08",
        "Graduale Romanum, 1961": "G.Rom '61",
        "Graduale Romanum, 1974": "G.Rom '74",
        "Graduale simplex, 1975": "G.Smp '75",
        "Gregorian Missal, 1990": "Gr.Mis '90",
        "Liber cantualis, 1983": "L.Cant '83",
    }
    meta_prop_keywords = [
        "name",
        "office",
        "mode",
        "book",
        "transcriber",
        "publisher",
    ]

    gabc_metadata = {}

    ## reading metadata
    with open(gabc_data_file) as cgdf:
        for cgd_line in cgdf:
            for m_prop_kw in meta_prop_keywords:
                if m_prop_kw in cgd_line:
                    meta_pair = cgd_line.split(":")
                    display_val = meta_pair[1][:-2]
                    if m_prop_kw is "book":
                        for s_full, s_abbrev in source_abbrevs.items():
                            display_val = display_val.replace(s_full, s_abbrev)
                        display_val = display_val.replace(" & ", ";  ")
                        display_val = display_val.replace(" p. ", " p.")
                    gabc_metadata[meta_pair[0]] = display_val

    print(f"gabc_metadata: {gabc_metadata}")
    return gabc_metadata


def lege_tabulae_gabc(doc_id, gabc_data_files):
    """Converts GABC files to LY"""
    doc_metadata = {}
    ctr_files = 1

    for gabc_data_file in gabc_data_files:
        inFilePath = os.path.join(cfg_data["data_dir"], gabc_data_file)

        doc_metadata[f"{doc_id}_{ctr_files}"] = get_gabc_metadata(inFilePath)
        ctr_files = ctr_files + 1

        # inFileName = os.path.basename(gabc_data_file)
        # outFileName = inFileName.replace(".gabc", "")
        # outFilePath = f"{cfg_data["output_dir_ly_data"]}/{outFileName}.ly"
        outFilePath = os.path.join(
            cfg_data["output_dir_ly_data"], gabc_data_file
        ).replace(".gabc", ".ly")
        outFileDir = Path(outFilePath).parent
        Path(outFileDir).mkdir(parents=True, exist_ok=True)

        cmdString = f"{cfg_data["gabctk_dir"]}/{cfg_data['gabctk_script_fname']} -i {inFilePath}  -l {outFilePath} -v"
        # cmdString = f"{cfg_data["gabctk_dir"]}/{cfg_data['gabctk_script_fname']} -i {gabc_data_file}  -l {outFilePath} -d 2 -v"
        print_frame(
            "USING GABCTK",
            cfg_data,
            {"cmdString": cmdString, "outFilePath": outFilePath},
        )

        try:
            retcode = subprocess.call(cmdString, shell=True)
            if retcode < 0:
                print("Child process terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child process returned", retcode, file=sys.stderr)
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)

    return doc_metadata


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
    elif "\\transpose" in subject_line:
        return "transpose"

    # ---------------------------
    #  PUNCTUATION

    elif "%" in subject_line:
        return "comment"
    elif "}" == subject_line:
        return "end_bracket"
    elif ">>" in subject_line:
        return "end_dbl_ang_bracket"
    else:
        return None


def copy_conv_gabc_vars(fname_slug, conv_ly_filepath, out_ly_path):
    """Reads and copies a file of converted LY code (from gabctk)"""
    ly_script_stack = []
    music_name = f"Music{fname_slug}"
    lyrics_name = f"Lyrics{fname_slug}"

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
    ly_transpose = "des"

    with open(conv_ly_filepath) as f:
        with open(out_ly_path, "a") as wr:
            for ly_line in f:
                script_evt_type = analyze_conv_gabc_line(ly_line)
                is_valid_copy = False
                if script_evt_type is not None:
                    if (
                        script_evt_type in bracket_delim_blocks
                        or script_evt_type in dbl_ang_bracket_delim_blocks
                    ):
                        ly_script_stack.append(script_evt_type)

                    if (
                        "musiquetheme" in ly_script_stack
                        or "paroles" in ly_script_stack
                    ):
                        is_valid_copy = True
                    elif script_evt_type is "transpose":
                        ly_transpose = ly_line.strip().replace(
                            "\cadenzaOn \\transpose c ", ""
                        )
                        ly_transpose = ly_transpose.replace("{\MusiqueTheme}", "")

                    if (
                        script_evt_type == "end_bracket"
                        and ly_script_stack[-1] in bracket_delim_blocks
                    ):
                        ly_script_stack.remove(ly_script_stack[-1])
                    elif (
                        script_evt_type == "end_dbl_ang_bracket"
                        and ly_script_stack[-1] in dbl_ang_bracket_delim_blocks
                    ):
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
                        ly_line = ly_line.replace('&zwj;*__', '')
                        ly_line = ly_line.replace('&zwj;*_', '')
                        ly_line = ly_line.replace('<nlba>', '')
                        ly_line = ly_line.replace('</nlba>', '')
                        ly_line = ly_line.replace('<eu>', '')
                        ly_line = ly_line.replace('</eu>', '')
                        ly_line = ly_line.replace('<sc>', '')
                        ly_line = ly_line.replace('</sc>', '')
                        wr.write(ly_line)
    return ly_transpose
