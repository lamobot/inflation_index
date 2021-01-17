# -*- coding: utf-8 -*-
"""This module returns index for housing sector"""

import requests
from bs4 import BeautifulSoup
import mysql.connector
import config


def get_url_response(url: str) -> object:
    """
    This function returns response object
    :param url: link to website which we're going to parse
    :return: response from server
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    return None


def get_links_from_database(category: tuple) -> list:
    """
    Return list of strings with urls for parsing
    :param category: one of this tuples:
        - ("globus products", )
    :return: list of urls
    """
    url_list = []
    conn = mysql.connector.connect(
        host=config.db_server,
        user=config.db_user,
        password=config.db_password,
        database=config.db_name
    )
    curs = conn.cursor()

    sql = """
        SELECT link FROM links l
        JOIN categories c ON l.categories_id = c.id
        WHERE c.name = %s
    """
    curs.execute(sql, category)
    result = curs.fetchall()
    for link in result:
        url_list.append(link[0])
    conn.close()
    return url_list
