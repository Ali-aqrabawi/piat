# (c) 2019, Ali Aqrabawi <aaqrabawn@gmail.com>
#
# This file is part of Piat
#
# Piat is free software licensed under MIT License.

import os
import sys

__version__ = '0.0.13'
__author__ = 'Ali Aqrabawi'

try:
    if not sys.version_info.major == 3:
        raise RuntimeError('piat requires Python3')
except AttributeError:
    raise RuntimeError('piat requires Python3')

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ["PIAT_MIB_PATH"] = os.path.join(DIR_PATH, 'mibs')
