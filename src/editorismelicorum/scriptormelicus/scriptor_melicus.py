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


def write_song_ly(song_filepath, template_filepath, doc_data):
    # read in template file, replace values in template, copy to song
    with open(template_filepath) as tf:
        with open(song_filepath, "a") as twr:
            for t_line in tf:
                template_line = t_line
                for key, value in template_replace_map.items():
                    template_line = template_line.replace(key, doc_data[value])
                twr.write(template_line)
            twr.write("\n\n")
    return 0
