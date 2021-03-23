# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import tabula
from config import *


def get_electricity_price(response: object) -> float:
    """
    Return price of electricity
    :param response: need function get_url_response from get_response module
    :return: electricity price in float format
    """
    return float(response.find(class_="d-table-num-left").text.replace(',', '.'))


def get_housing_service_price(filename: str) -> float:
    """
    Return price of other housing service
    :param filename
    :return: price of other housing service in float format
    """
    table = tabula.read_pdf(filename, pages=1)
    tbl = table[2]
    housing_price = 0.0
    # print(tbl[10:18]['Unnamed: 2'])
    # for item in tbl[10:18]['Unnamed: 2']:
        # print(item)
        # housing_price += float(item.replace(',', '.'))
    # print(tbl[['Unnamed: 0', 'Unnamed: 2']][10:18].values)
    for k, v in tbl[['Unnamed: 0', 'Unnamed: 2']][10:18].values:
        # if k == '43,400':
        print(k, '=>', v)
    # return round(housing_price, 2)


get_housing_service_price(FILENAME)