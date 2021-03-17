# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from tabula.io import read_pdf
from config import *
from libs import get_url_response


def get_electricity_price(response: object) -> float:
    """
    Return price of electricity
    :param response: need function get_url_response from get_response module
    :return: electricity price in float format
    """
    return float(response.find(class_="d-table-num-left").text.replace(',', '.')) * ELECTRICITY_COUNTER


def get_housing_service_price(filename: str) -> float:
    """
    Return price of other housing service
    :param filename
    :return: price of other housing service in float format
    """
    try:
        table = read_pdf(filename, pages=1)
        tbl = table[2]
        housing_price = 0.0
        for item in tbl[10:18]['Unnamed: 2']:
            housing_price += float(item.replace(',', '.'))
        return round(housing_price, 2)
    except FileNotFoundError:
        print('There is no file for housings service')


def calculate_housing_sector_index() -> float:
    try:
        return get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)) + \
            get_housing_service_price(HOUSING_SECTOR_BILL_FILE)
    except Exception as err:
        print('Something went wrong:', str(err))
        return 'ERROR'


print(get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)))
