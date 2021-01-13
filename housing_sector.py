# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import re
from get_response import get_url_response

URL_TO_PARSE_ELECTRICITY_PRICE = "https://www.mosenergosbyt.ru/individuals/tariffs-n-payments/" \
                                 "tariffs-mo/kvartiry-i-doma-s-elektricheskimi-plitami-mo.php"


def get_electricity_price(response: object) -> float:
    print(response.find_all('div'))





    # pattern = re.compile(r'«Пригород» – ')
    # result_string = response.find(text=pattern)
    # return float(re.findall(r'\d+', str(result_string.next_element))[0])


get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE))
