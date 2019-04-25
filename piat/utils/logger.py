import os
import logging

formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s:%(lineno)s : %(message)s')

if not os.path.exists('./logs'):
    os.makedirs('./logs')


def get_logger(file_name):
    LOGGER = logging.getLogger(file_name)
    LOGGER.setLevel(logging.DEBUG)
    file_hdlr = logging.FileHandler('./logs/%s' % file_name.replace('.','_'))
    file_hdlr.setFormatter(formatter)
    LOGGER.addHandler(file_hdlr)
    return LOGGER
