# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

from libs import get_url_response, write_logs
import csv
import re


def get_product_price(link: str, shop: str) -> float:
    soup = get_url_response(link)
    if soup is None:
        write_logs('unavailable product - {}'.format(link), 'ERROR')
        raise Exception('unavailable product - ' + link)
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
        if row['shop'] == shop:
            product_price = get_product_price(row['product_url'], shop)
            product_dict[row['product_name']] = product_price
    return product_dict


def calculate_index(shop1: dict, shop2: dict, shop3: dict) -> dict:
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


print(get_product_dict_from_csv('list.csv', 'vprok'))
print(get_product_dict_from_csv('list.csv', 'globus'))
print(get_product_dict_from_csv('list.csv', 'aushan'))

print(calculate_index(get_product_dict_from_csv('list.csv', 'vprok'), get_product_dict_from_csv('list.csv', 'globus'),
                get_product_dict_from_csv('list.csv', 'aushan')))

