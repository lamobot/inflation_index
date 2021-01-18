# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import tabula


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
    for item in tbl[10:18]['Unnamed: 2']:
        housing_price += float(item.replace(',', '.'))
    return round(housing_price, 2)
