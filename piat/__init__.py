import os
import sys

__version__ = '0.0.1'
__author__ = 'Ali Aqrabawi'


try:
    if not sys.version_info.major == 3:
        raise RuntimeError('piat requires Python3')
except AttributeError:
    raise RuntimeError('piat requires Python3')

dir_path = os.path.dirname(os.path.realpath(__file__))
os.environ["PIAT_MIB_PATH"] = os.path.join(dir_path, 'mibs')
