# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from libs import get_links_from_database, get_url_response
import logging


logging.basicConfig(filename='script.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(funcName)s:  %(message)s')


def get_product_index_from_globus(links: list) -> float:
    product_index_cost = 0.0
    for link in links:
        soup = get_url_response(link)
        if soup is None:
            logging.error('unavailable product - ' + link)
            raise Exception('unavailable product - ' + link)
        price = float(soup.select_one("div.item-card__content--right span.item-price__rub").text + '.' +
                      soup.select_one("div.item-card__content--right span.item-price__kop").text)
        product_index_cost += price
    logging.info('Product index of Globus shop has been calculated successfully')
    return round(product_index_cost, 2)


def get_product_index_from_vprok(links: list) -> float:
    product_index_cost = 0.0
    for link in links:
        soup = get_url_response(link)
        if soup is None:
            logging.error('unavailable product - ' + link)
            raise Exception('unavailable product - ' + link)
        if soup.select_one("div.xf-product-new__temporarily-out-of-stock"):
            logging.error('The product is temporarily out of stock - ' + link)
            raise Exception('The product is temporarily out of stock - ' + link)
        price = float(soup.select_one("span.js-price-rouble").text +
                      soup.select_one("span.js-price-penny").text.replace(',', '.'))
        product_index_cost += price
    logging.info('Product index of vprok shop has been calculated successfully')
    return round(product_index_cost, 2)


if __name__ == "__main__":
    print(get_product_index_from_globus(get_links_from_database(("globus products", ))))
    print(get_product_index_from_vprok(get_links_from_database(("vprok products", ))))

