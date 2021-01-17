# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import logging
from libs import get_links_from_database, get_url_response


logging.basicConfig(filename='script.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(funcName)s:  %(message)s')


def get_product_index_from_globus(links: list) -> float:
    """
    Return Globus product index
    :param links: list of globus links
    :return: globus product index in float format
    """
    product_index_cost = 0.0
    for link in links:
        soup = get_url_response(link)
        if soup is None:
            logging.error('unavailable product - %s', link)
            raise Exception('unavailable product - ' + link)
        price = float(soup.select_one("div.item-card__content--right span.item-price__rub").text
                      + '.' +
                      soup.select_one("div.item-card__content--right span.item-price__kop").text)
        product_index_cost += price
    logging.info('Product index of Globus shop has been calculated successfully')
    return round(product_index_cost, 2)


def get_product_index_from_vprok(links: list) -> float:
    """
    Return Perekrestok product index
    :param links: list of perekrestok links
    :return: perekrestok product index in float format
    """
    product_index_cost = 0.0
    for link in links:
        soup = get_url_response(link)
        if soup is None:
            logging.error('unavailable product - %s', link)
            raise Exception('unavailable product - ' + link)
        if soup.select_one("div.xf-product-new__temporarily-out-of-stock"):
            logging.error('The product is temporarily out of stock - %s', link)
            raise Exception('The product is temporarily out of stock - ' + link)
        price = float(soup.select_one("span.js-price-rouble").text +
                      soup.select_one("span.js-price-penny").text.replace(',', '.'))
        product_index_cost += price
    logging.info('Product index of vprok shop has been calculated successfully')
    return round(product_index_cost, 2)


if __name__ == "__main__":
    print(get_product_index_from_globus(get_links_from_database(("globus products", ))))
    print(get_product_index_from_vprok(get_links_from_database(("vprok products", ))))
