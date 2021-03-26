# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import tabula
from config import FILENAME


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
    table = tabula.read_pdf(filename, pages=1, pandas_options={'header': None})
    tbl = table[2]
    dct = {}
    for item in tbl.values:
        # dct[item[0]] = [float(item[1].replace(',', '.')), float(item[3].replace(',', '.'))]
        if item[1] == '43,400':
            dct[item[0]] = round(float(item[1].replace(',', '.')) * float(item[3].replace(',', '.')), 2)
        elif item[0] == 'Телеантенна':
            dct[item[0]] = round(float(item[3].replace(',', '.')), 2)
        elif item[0] == 'ГВС':
            dct[item[0]] = round(float(item[3].replace(',', '.')) * 3, 2)

    print(dct)


    # for item in tbl.values[10:18]:
    #     print(str(item).strip().split(' '))
    # for k, v in tbl[['Unnamed: 0', 'Unnamed: 2']][10:18].values:
    #     dct[k] = v
    # print(dct)


if __name__ == "__main__":
    get_housing_service_price(FILENAME)
