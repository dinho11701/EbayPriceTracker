# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests
<<<<<<< HEAD
=======
import re
>>>>>>> 4d83461 (Functions added to have the lower price)
import numpy as np
import csv
from datetime import datetime

<<<<<<< HEAD
LINK = "https://www.ebay.co.uk"
=======
LINK = "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=airpods+pro&_sacat=0&LH_TitleDesc=0&_odkw=macbook+pro&_osacat=0"
>>>>>>> 4d83461 (Functions added to have the lower price)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


<<<<<<< HEAD
=======
def get_prices_by_link(link):
    r = requests.get(link)
    page_parse = BeautifulSoup(r.text,'html.parser')

    search_results = page_parse.find("ul",{"class":"srp-results"}).find_all("li",{"class":"s-item"})

    items_prices = []

    for result in search_results:
        price_as_text = result.find("span",{"class":"s-item__price"}).text
        if "to" in price_as_text:
            continue
        #price = float(price_as_text.strip()[1:].replace(",", ""))
        price_str = re.sub(r'[^\d.]', '', price_as_text)
        price = float(price_str)
        items_prices.append(price)

    return items_prices

#cette fonction permet de filtrer les valeurs aberrantes
# (valeurs extrêmes) dans une liste de prix en utilisant
# la méthode des écarts-types. Elle retourne une nouvelle
# liste ne contenant que les valeurs qui sont à l'intérieur
# d'une certaine plage définie par la moyenne et l'écart-type
# des prix.
def remove_outlies(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

#fais la moyenne des prix d'une liste
def get_average(prices):
    return np.mean(prices)


def save_to_file(prices):
    fields = [datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv','a',newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

>>>>>>> 4d83461 (Functions added to have the lower price)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

<<<<<<< HEAD
=======
    price = get_prices_by_link(LINK)
    prices_filtred = remove_outlies(price)
    print(get_average(prices_filtred))

>>>>>>> 4d83461 (Functions added to have the lower price)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
