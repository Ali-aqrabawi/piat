import os
import logging
import sys

FILE_FORMATTER = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s:%(lineno)s : %(message)s')
STDOUT_FORMATTER = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
if not os.path.exists('./logs'):
    os.makedirs('./logs')


def get_logger(file_name):
    LOGGER = logging.getLogger(file_name)
    LOGGER.setLevel(logging.INFO)
    file_hdlr = logging.FileHandler('./logs/%s' % file_name.replace('.', '_'))
    file_hdlr.setFormatter(FILE_FORMATTER)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(STDOUT_FORMATTER)

    LOGGER.addHandler(file_hdlr)
    LOGGER.addHandler(stream_handler)
    return LOGGER
