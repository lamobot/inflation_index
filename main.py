# -*- coding: utf-8 -*-
"""Main module"""

from transportation import calculate_transportation_index
from housing_sector import calculate_housing_sector_index
from products import calculate_product_index
from config import INDEX_CSV_FILE
import csv
import datetime

date = datetime.datetime.now()


def main() -> None:
    """
    This function writes indexes to csv file
    """
    with open(INDEX_CSV_FILE, 'a', newline='\n') as csvfile:
        record = csv.writer(csvfile, delimiter=',', quotechar='|')
        record.writerow([date.strftime("%Y-%m-%d"), calculate_transportation_index(),
                         calculate_housing_sector_index(), calculate_product_index()])


if __name__ == "__main__":
    main()
