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
    # 1. read in var file, copy to song
    with open(var_filepath) as f:
        with open(song_filepath, "w") as wr:
            for ly_line in f:
                wr.write(ly_line)
            wr.write("\n")

    # 2. read in template file, replace values in template, copy to song
    with open(template_filepath) as tf:
        with open(song_filepath, "a") as twr:
            for t_line in tf:
                template_line = t_line
                for key, value in template_replace_map.items():
                    template_line = template_line.replace(key, doc_data[value])
                twr.write(template_line)
    return 0
