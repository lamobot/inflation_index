# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import requests
from bs4 import BeautifulSoup


def get_url_response(url: str) -> object:
    """
    This function returns response object
    :param url: link to website which we're going to parse
    :return: response from server
    """
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")
