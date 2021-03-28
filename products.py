# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from libs import get_url_response, write_logs
from config import PRODUCTS_CSV_FILE
import csv
import re


def get_product_price(link: str, shop: str) -> float:
    soup = get_url_response(link)
    if soup is None:
        write_logs('unavailable product - {}'.format(link), 'ERROR')
    if shop == 'globus':
        return float(soup.select_one("div.item-card__content--right span.item-price__rub").text
                     + '.' +
                     soup.select_one("div.item-card__content--right span.item-price__kop").text)
    if shop == 'vprok':
        return float(soup.select_one("span.js-price-rouble").text +
                     soup.select_one("span.js-price-penny").text.replace(',', '.'))
    if shop == 'aushan':
        price = soup.select_one("div.fullPricePDP").text.replace(' ', '')
        price = re.search(r"\A\d+\.\d\d", price)
        return float(price.group())


def get_product_dict_from_csv(filename: str, shop: str) -> dict:
    product_dict = {}
    input_file = csv.DictReader(open(filename))
    for row in input_file:
        if row['shop_name'] == shop:
            product_price = get_product_price(row['product_url'], shop)
            product_dict[row['product_name']] = product_price * int(row['counter'])
    return product_dict


def get_average_product_price(shop1: dict, shop2: dict, shop3: dict) -> dict:
    """
    This function calculates average price of products between three shops
    :param shop1: First e-shop
    :param shop2: Second e-shop
    :param shop3: Third e-shop
    :return: dict of products and their prices
    """
    product_dict = {}
    product_set = set()
    product_set.update(set(shop1.keys()), set(shop2.keys()), set(shop3.keys()))
    for product_name in product_set:
        if product_name in shop1.keys() and product_name in shop2.keys() and product_name in shop3.keys():
            product_dict[product_name] = round((shop1[product_name] + shop2[product_name] + shop3[product_name]) / 3, 2)
        elif product_name in shop1.keys() and product_name in shop2.keys():
            product_dict[product_name] = round((shop1[product_name] + shop2[product_name]) / 2, 2)
        elif product_name in shop1.keys() and product_name in shop3.keys():
            product_dict[product_name] = round((shop1[product_name] + shop3[product_name]) / 2, 2)
        elif product_name in shop2.keys() and product_name in shop3.keys():
            product_dict[product_name] = round((shop2[product_name] + shop3[product_name]) / 2, 2)
        elif product_name in shop1.keys():
            product_dict[product_name] = shop1[product_name]
        elif product_name in shop2.keys():
            product_dict[product_name] = shop2[product_name]
        elif product_name in shop3.keys():
            product_dict[product_name] = shop3[product_name]
        else:
            product_dict["key"] = "bug"
    return product_dict


def calculate_product_index() -> float:
    """
    This function calculates product index and returns average price of products from globus, aushan and vprok shops
    """
    product_index = 0.0
    for price in get_average_product_price(get_product_dict_from_csv(PRODUCTS_CSV_FILE, 'vprok'),
                                           get_product_dict_from_csv(PRODUCTS_CSV_FILE, 'globus'),
                                           get_product_dict_from_csv(PRODUCTS_CSV_FILE, 'aushan')).values():
        product_index += price
    return round(product_index, 2)


if __name__ == '__main__':
    print(calculate_product_index())
