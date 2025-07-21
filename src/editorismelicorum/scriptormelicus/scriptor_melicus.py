#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Engraver of Music gets all the packaged info written out and ready for publishing.

import os
from pathlib import Path

from ed_melicorum_utils import print_frame, get_cfg_data

template_replace_map = {
    "TemplateTitle": "Title",
    "TemplateSubtitle": "Subtitle",
    "TemplateInstrument": "Instrument",
    "TemplateComposer": "Composer",
    "TemplateArranger": "Arranger",
    "TemplateLyricsLink": "LyricsLink",
    "TemplateMusic": "Music",
    "TemplateLyrics": "Lyrics",
}


def write_song_ly(song_filepath, var_filepath, template_filepath, doc_data):
    print("yerrr")

    # 1. read in var file, copy to song
    with open(var_filepath) as f:
        with open(song_filepath, "w") as wr:
            for ly_line in f:
                wr.write(ly_line)

    # 2. read in template file
    with open(template_filepath) as tf:
        for t_line in f:
            template_line = t_line

    # 3. read document data, replace values in template, copy to song

    return 0
