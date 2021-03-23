# -*- coding: utf-8 -*-
"""Main module"""

from transportation import calculate_transportation_index


def main() -> tuple:
    """
    This function calculates indexes
    :return: tuple of product, fuel and housing sector index
    """
    print(calculate_transportation_index())


if __name__ == "__main__":
    print(main())


