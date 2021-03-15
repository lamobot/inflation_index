import csv


globus = {
    "chocolate": 120,
    "bread": 50,
    "chicken": 220,
    "water": 80,
}

aushan = {
    "meat": 320,
    "chicken": 200,
    "water": 70,
}

vprok = {
    "bread": 60,
    "chicken": 250,
    "chocolate": 100,
}


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
            product_dict[product_name] = round((shop1[product_name] + shop2[product_name] + shop3[product_name]) / 3)
        elif product_name in shop1.keys() and product_name in shop2.keys():
            product_dict[product_name] = round((shop1[product_name] + shop2[product_name]) / 2)
        elif product_name in shop1.keys() and product_name in shop3.keys():
            product_dict[product_name] = round((shop1[product_name] + shop3[product_name]) / 2)
        elif product_name in shop2.keys() and product_name in shop3.keys():
            product_dict[product_name] = round((shop2[product_name] + shop3[product_name]) / 2)
        elif product_name in shop1.keys():
            product_dict[product_name] = shop1[product_name]
        elif product_name in shop2.keys():
            product_dict[product_name] = shop2[product_name]
        elif product_name in shop3.keys():
            product_dict[product_name] = shop3[product_name]
        else:
            product_dict["key"] = "bug"
    return product_dict


def get_product_dict_from_csv(filename: str, shop: str) -> dict:
    product_dict = {}
    input_file = csv.DictReader(open(filename))
    for row in input_file:
        if row['shop'] == shop:
            product_dict[row['product_name']] = row['product_url']
    return product_dict


# print(calculate_index(globus, aushan, vprok))
print(get_product_dict_from_csv('list.csv', 'vprok'))