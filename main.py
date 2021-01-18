from libs import get_links_from_database, get_url_response, insert_calculated_index_to_database
from fuel_prices import get_fuel_price, get_mcd_ticket_price
from products import get_product_index_from_globus, get_product_index_from_vprok
from housing_sector import get_housing_service_price, get_electricity_price

FILENAME = 'tmp/bill.pdf'
URL_TO_PARSE_FUEL = "https://auto.mail.ru/fuel/"
URL_TO_PARSE_MCD_TICKETS = "https://troikarta.ru/tarify/mcd/"
URL_TO_PARSE_ELECTRICITY_PRICE = "https://www.mosenergosbyt.ru/individuals/tariffs-n-payments/" \
                                 "tariffs-mo/kvartiry-i-doma-s-elektricheskimi-plitami-mo.php"


def calculate_index() -> tuple:
    product_index = (get_product_index_from_globus(get_links_from_database(("globus products",))) +
                     get_product_index_from_vprok(get_links_from_database(("vprok products",)))) / 2

    fuel_index = get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'ai95') + \
        get_fuel_price(get_url_response(URL_TO_PARSE_FUEL), 'dt') + \
        get_mcd_ticket_price(get_url_response(URL_TO_PARSE_MCD_TICKETS))

    housing_sector_index = get_electricity_price(get_url_response(URL_TO_PARSE_ELECTRICITY_PRICE)) + \
        get_housing_service_price(FILENAME)

    return product_index, fuel_index, housing_sector_index,


if __name__ == "__main__":
    insert_calculated_index_to_database(calculate_index())
