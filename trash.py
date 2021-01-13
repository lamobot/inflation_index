def get_train_ticket_price(url: str) -> float:
    """
    This function returns RZD ticket prices, but I don't know, how theirs prices work.
    I'm not going to use this function now
    :param url:
    :return:
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    if json.loads(data):
        result_string = json.loads(data)['trips']
    for item in result_string:
        if item['trainNumber'] == '738Я':
            return float(item['categories'][0]['price'])

DATE = (datetime.now() + timedelta(days=calendar.monthrange(datetime.now().year,
                                                            datetime.now().month)[1])).strftime("%Y-%m-%d")

URL_TO_PARSE_RZD_TICKETS = "https://suggest.travelpayouts.com/search?service=tutu_trains&term=2000001&term2=2010050"