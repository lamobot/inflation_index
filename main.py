# -*- coding: utf-8 -*-
"""Main module"""

from config import *
from libs import get_url_response
from housing_sector import get_housing_service_price, get_electricity_price


def main() -> tuple:
    """
    This function calculates indexes
    :return: tuple of product, fuel and housing sector index
    """

    housing_sector_index = get_electricity_price(
        get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)
    ) + get_housing_service_price(FILENAME)

    return fuel_index, housing_sector_index


if __name__ == "__main__":
    print(main())


