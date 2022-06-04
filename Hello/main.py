from datetime import datetime

import pandas
import requests


def fetch_price(start_city, arr_city):
    show_data_cot = 10
    time_format = "%Y%m%d"
    url = "https://flights.ctrip.com/itinerary/api/12808/lowestPrice?flightWay=Oneway&direct=true&army=false"
    url = url + "&dcity=" + start_city + "&acity=" + arr_city
    res = requests.get(url)
    res.encoding = "utf-8"

    prices = pandas.read_json(res.text)
    date_price_map = list(prices['data']['oneWayPrice'])[0]

    date_price_map = sorted(date_price_map.items(), key=lambda item: item[1])
    create_file = open(datetime.now().strftime(time_format), "a", encoding="utf-8")

    print("from [" + str(start_city) + "] to [" + str(arr_city) + "]")

    create_file.write("from [" + str(start_city) + "] to [" + str(arr_city) + "]")
    create_file.write("\n")
    create_file.write(str(datetime.now()))
    create_file.write("\n")

    show_cot = 1
    for i in date_price_map:
        date_price = str(i[0]) + ":" + str(i[1])
        print(date_price)
        create_file.write(date_price)
        create_file.write("\n")
        show_cot = show_cot + 1
        if show_cot >= show_data_cot:
            break
    create_file.close()


if __name__ == '__main__':
    start_city = "NGB"
    arr_city = "CSX"
    fetch_price(start_city, arr_city)
    arr_city = "CKG"
    fetch_price(start_city, arr_city)
