# -*- coding: utf-8 -*-
"""This module returns index for transportation"""

import re
from libs import write_logs, get_url_response
from config import FUEL_LITTERS_PER_MONTH, TRAIN_TICKETS_PER_MONTH, URL_TO_PARSE_FUEL, MCD_PRICE


def get_fuel_price(response: object, fuel_type: str = 'ai95') -> float:
    """
    This function returns fuel prices
    :param response: response object from get_url_response function
    :param fuel_type: ai95 or dt
    :return fuel price: price in rubles in float format
    """
    pattern = re.compile(r'var toolbarFuel =')
    result_string = response.find("script", text=pattern)
    if fuel_type == 'ai95':
        search_string = r'"value":\d+\.\d+,"type":"95"'
    elif fuel_type == 'dt':
        search_string = r'"value":\d+\.\d+,"type":"dt"'
    else:
        raise ValueError('We can parse only \"ai95\" or \"dt\"')
    fuel_price = re.search(search_string, str(result_string))
    write_logs('Fuel price index has been calculated successfully', 'INFO')
    return float(fuel_price.group(0).split(',')[0].split(':')[1])


def calculate_transportation_index() -> float:
    """
    This function calculates transportation index and returns sum of fuel and mcd tickets prices per month
    """
    return round((get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'ai95') * FUEL_LITTERS_PER_MONTH) + \
                 (get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'dt') * FUEL_LITTERS_PER_MONTH) + \
                 (MCD_PRICE * TRAIN_TICKETS_PER_MONTH), 2)


if __name__ == "__main__":
    print(MCD_PRICE * TRAIN_TICKETS_PER_MONTH)
    print(get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'ai95') * FUEL_LITTERS_PER_MONTH)
    print(get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'dt') * FUEL_LITTERS_PER_MONTH)
    print(calculate_transportation_index())
