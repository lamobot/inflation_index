# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import logging
import requests
from bs4 import BeautifulSoup
# TODO loguru

logging.basicConfig(filename='script.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(funcName)s:  %(message)s')


def write_logs(message: str, level: str) -> object:
    """
    Write logs to script.log
    :param message: log message in string format
    :param level: ERROR or INFO log level in string format
    :return:
    """
    if level == 'ERROR':
        return logging.error(message)
    return logging.info(message)


def get_url_response(url: str) -> object:
    """
    This function returns response object
    :param url: link to website which we're going to parse
    :return: response from server
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    return None
