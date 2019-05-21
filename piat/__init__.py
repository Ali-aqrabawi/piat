# (c) 2019, Ali Aqrabawi <aaqrabawn@gmail.com>
#
# This file is part of Piat
#
# Piat is free software licensed under MIT License.

import sys

__version__ = '0.0.15'
__author__ = 'Ali Aqrabawi'

try:
    if not sys.version_info.major == 3:
        raise RuntimeError('piat requires Python3')
except AttributeError:
    raise RuntimeError('piat requires Python3')
