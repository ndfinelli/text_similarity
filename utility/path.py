#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os


def use_project_path():
    """
    Based on the path of this file, we change directory to the project root.  This is used in the scripts to ensure
    path resolution is done the same when files are run through the IDE and command line.
    :return:
    """
    path = re.sub(
        '[\\\\/]utility[\\\\/]path\\.py$',
        '',
        __file__
    )
    os.chdir(path)