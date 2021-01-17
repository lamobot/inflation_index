# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import tabula
from libs import get_url_response


FILENAME = 'tmp/bill.pdf'
URL_TO_PARSE_ELECTRICITY_PRICE = "https://www.mosenergosbyt.ru/individuals/tariffs-n-payments/" \
                                 "tariffs-mo/kvartiry-i-doma-s-elektricheskimi-plitami-mo.php"


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


def count_index_points() -> float:
    """
    This function returns housing sector index points
    :return: HSIP
    """
    return get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)) + \
        get_housing_service_price(FILENAME)


print(count_index_points())
