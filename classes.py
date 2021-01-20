# -*- coding: utf-8 -*-
"""Library with classes"""

import mysql.connector as mysql
import config


class ConnectToDatabase:
    """
    Database connection
    """

    def __init__(self):
        self.conn = mysql.connect(
            host=config.DB_SERVER,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )

    def get_links_from_database(self, category: tuple) -> list:
        """
        Return list of strings with urls for parsing
        :param category: one of this tuples:
            - ("globus products", )
            - ("vprok products", )
        :return: list of urls
        """
        url_list = []
        curs = self.conn.cursor()

        sql = """
            SELECT link FROM links l
            JOIN categories c ON l.categories_id = c.id
            WHERE c.name = %s
        """
        curs.execute(sql, category)
        result = curs.fetchall()
        for link in result:
            url_list.append(link[0])
        return url_list

    def insert_calculated_index_to_database(self, calculated_index: tuple) -> None:
        """
        This function inserts calculated index to database
        :param calculated_index: Tuple of calculated indexes
        :return: None
        """
        curs = self.conn.cursor()

        sql = """
            INSERT INTO indexes (transportation_index, housing_sector_index, product_index)
            VALUES (%s, %s, %s)
            """
        curs.execute(sql, calculated_index)
        self.conn.commit()

    def close_connection(self) -> None:
        """
        This function closes connection to mysql server
        :return: None
        """
        self.conn.close()
        self.conn.cursor().close()
