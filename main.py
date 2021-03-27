# -*- coding: utf-8 -*-
"""Main module"""

from transportation import calculate_transportation_index
from housing_sector import calculate_housing_sector_index


def main() -> tuple:
    """
    This function calculates indexes
    :return: tuple of product, fuel and housing sector index
    """
    return calculate_transportation_index() + calculate_housing_sector_index()


if __name__ == "__main__":
    print(main())


