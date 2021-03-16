# -*- coding: utf-8 -*-
"""Main module"""

from libs import get_url_response
from fuel_prices import get_fuel_price, get_mcd_ticket_price
from housing_sector import get_housing_service_price, get_electricity_price

FILENAME = 'tmp/bill.pdf'
URL_TO_PARSE_FUEL = "https://auto.mail.ru/fuel/"
URL_TO_PARSE_MCD_TICKETS = "https://troikarta.ru/tarify/mcd/"
URL_TO_PARSE_ELECTRICITY_PRICE = "https://www.mosenergosbyt.ru/individuals/tariffs-n-payments/" \
                                 "tariffs-mo/kvartiry-i-doma-s-elektricheskimi-plitami-mo.php"


def main() -> tuple:
    """
    This function calculates indexes
    :return: tuple of product, fuel and housing sector index
    """

    fuel_index = get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'ai95') + \
        get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'dt') + \
        get_mcd_ticket_price(get_url_response(URL_TO_PARSE_MCD_TICKETS))

    housing_sector_index = get_electricity_price(
        get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)
    ) + get_housing_service_price(FILENAME)

    return fuel_index, housing_sector_index


if __name__ == "__main__":
    pass


