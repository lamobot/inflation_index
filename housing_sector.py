# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from tabula import read_pdf
from config import HOUSING_SECTOR_BILL_FILE, COLD_WATER_AVERAGE_CONSUMPTION, HOT_WATER_AVERAGE_CONSUMPTION, \
    ELECTRICITY_COUNTER, ELECTRICITY_PRICE


def get_housing_service_price(filename: str) -> float:
    """
    This functions returns average price of housing sector
    :param filename
    :return: price of other housing service in float format
    """
    table = read_pdf(filename, pages=1, pandas_options={'header': None})
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


def calculate_housing_sector_index() -> float:
    """
    This function calculates housing sector index and returns sum of electricity and housing service prices
    """
    return round(get_housing_service_price(HOUSING_SECTOR_BILL_FILE) + \
                 (ELECTRICITY_COUNTER * ELECTRICITY_PRICE), 2)


if __name__ == "__main__":
    print(get_housing_service_price(HOUSING_SECTOR_BILL_FILE))
    print(ELECTRICITY_COUNTER * ELECTRICITY_PRICE)
    print(calculate_housing_sector_index())
