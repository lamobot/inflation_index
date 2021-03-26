# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import tabula
from libs import get_url_response
from config import FILENAME, COLD_WATER_AVERAGE_CONSUMPTION, HOT_WATER_AVERAGE_CONSUMPTION, \
    URL_TO_PARSE_ELECTRICITY_PRICE


def get_electricity_price(response: object) -> float:
    """
    Return price of electricity
    :param response: need function get_url_response from get_response module
    :return: electricity price in float format
    """
    return float(response.find(class_="d-table-num-left").text.replace(',', '.'))


def get_housing_service_price(filename: str) -> float:
    """
    This functions returns average price of housing sector
    :param filename
    :return: price of other housing service in float format
    """
    table = tabula.read_pdf(filename, pages=1, pandas_options={'header': None})
    tbl = table[2]
    housing_service_cost_sum = 0.0

    def cost_sum(cost_volume: str, cost_tariff: str, avg_counter: int = 1) -> float:
        """
        This function converts tabula series to float
        :param cost_volume:
        :param cost_tariff:
        :param avg_counter:
        :return: float cost_sum
        """
        if avg_counter == 1:
            return round(float(cost_volume.replace(',', '.')) * float(cost_tariff.replace(',', '.')) * avg_counter, 2)
        return round(float(cost_tariff.replace(',', '.')) * avg_counter, 2)

    for item in tbl.values:
        if item[0] in ('Техобслуживание', 'Отопление', 'Телеантенна', 'Капитальный ремонт', 'Вывоз и утилизация ТКО'):
            housing_service_cost_sum += cost_sum(item[1], item[3])
        elif item[0] == 'ГВС':
            housing_service_cost_sum += cost_sum(item[1], item[3], HOT_WATER_AVERAGE_CONSUMPTION)
        elif item[0] == 'ХВС':
            housing_service_cost_sum += cost_sum(item[1], item[3], COLD_WATER_AVERAGE_CONSUMPTION)
        elif item[0] == 'Водоотведение':
            housing_service_cost_sum += cost_sum(item[1], item[3], (HOT_WATER_AVERAGE_CONSUMPTION +
                                                                    COLD_WATER_AVERAGE_CONSUMPTION))
    return round(housing_service_cost_sum, 2)


if __name__ == "__main__":
    print(get_housing_service_price(FILENAME))
    print(get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)))
