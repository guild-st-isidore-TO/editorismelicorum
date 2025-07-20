#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Reader of Music is in charge of re-copying music from outside.

# import sys
# import subprocess
# import json
# import os
# from pathlib import Path

from .. import ed_melicus_utils


def mark_conv_gabc_line(conv_ly_line, action, data):
    """Use the given action and data to do something with the LY line"""
    return 0


def analyze_conv_gabc_line(conv_ly_line):
    """Checks a line of converted LY code (from gabctk) for certain features. Decides the appropriate action based on string patterns."""

    # ---------------
    #  DECLARATIONS

    if "\\version" in conv_ly_line:
        return "version"
    if "\\midi{}" in conv_ly_line:
        return "midi"
    elif "\\header" in conv_ly_line:
        return "header_start"
    elif "\\paper" in conv_ly_line:
        return "paper_start"

    # ---------------
    #  VARIABLES

    elif "MusiqueTheme" in conv_ly_line:
        return "musiquetheme_start"
    elif "Paroles" in conv_ly_line:
        return "paroles_start"

    # ---------------------------
    #  SCORE CREATION

    elif "\\score" in conv_ly_line:
        return "score_start"
    elif "  <<" in conv_ly_line:
        return "staffgroup_start"
    elif "\\new Staff <<" in conv_ly_line:
        return "staff_start"
    elif "\\new Voice" in conv_ly_line:
        return "voice_start"
    elif "\\new Lyrics" in conv_ly_line:
        return "lyrics_start"
    elif "\\layout" in conv_ly_line:
        return "layout_start"
    elif "\\context" in conv_ly_line:
        return "context_start"
    elif "%" in conv_ly_line:
        return "comment"
    elif "}" in conv_ly_line:
        return "end_bracket"
    elif ">>" in conv_ly_line:
        return "end_dbl_ang_bracket"
    else:
        return None


def read_conv_gabc(conv_ly_filepath):
    """Reads a file of converted LY code (from gabctk)"""
    ly_script_stack = []

    bracket_delim_blocks = [
        "score_start",
        "lyrics_start",
        "layout_start",
        "voice_start",
        "context_start",
    ]

    dbl_ang_bracket_delim_blocks = ["staffgroup_start", "staff_start"]

    with open(conv_ly_filepath) as f:
        for line in f:
            script_evt_type = analyze_conv_gabc_line(line)
            if script_evt_type is not None:
                if (
                    script_evt_type == "end_bracket"
                    and ly_script_stack[-1] in bracket_delim_blocks
                ):
                    print("Found end of block")
                elif (
                    script_evt_type == "end_dbl_ang_bracket"
                    and ly_script_stack[-1] in dbl_ang_bracket_delim_blocks
                ):
                    print("Found end of block")
    return 0
