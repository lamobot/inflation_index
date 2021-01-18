# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from libs import get_url_response, write_logs


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
            write_logs('unavailable product - {}'.format(link), 'ERROR')
            raise Exception('unavailable product - ' + link)
        price = float(soup.select_one("div.item-card__content--right span.item-price__rub").text
                      + '.' +
                      soup.select_one("div.item-card__content--right span.item-price__kop").text)
        product_index_cost += price
    write_logs('Product index of Globus shop has been calculated successfully', 'INFO')
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
            write_logs('unavailable product - {}'.format(link), 'ERROR')
            raise Exception('unavailable product - ' + link)
        if soup.select_one("div.xf-product-new__temporarily-out-of-stock"):
            write_logs('The product is temporarily out of stock - {}'.format(link), 'ERROR')
            raise Exception('The product is temporarily out of stock - ' + link)
        price = float(soup.select_one("span.js-price-rouble").text +
                      soup.select_one("span.js-price-penny").text.replace(',', '.'))
        product_index_cost += price
    write_logs('Product index of Vptok shop has been calculated successfully', 'INFO')
    return round(product_index_cost, 2)
