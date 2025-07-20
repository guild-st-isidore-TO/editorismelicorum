#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Engraver of Music gets all the packaged info written out and ready for publishing.

import os
from pathlib import Path

from ed_melicus_utils import print_frame, get_cfg_data

# ---------------
# CONFIGURATION

file_dir = os.path.dirname(os.path.realpath(__file__))
cfg_data = get_cfg_data()
print_frame("WIP - SCRIPTOR MELICUS", cfg_data)
