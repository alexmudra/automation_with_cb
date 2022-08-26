#м map - приймає як параметр фукцію як обєкт
#приклад:
# def go_map (a):
#     return a**2
# some_lst = [1, 2 , 3 , 4]
# do_map = (map(go_map, some_lst))
# print(list(do_map)) #результат print(list(do_map))

###################### 2 #############################

import requests


def capital_lettered_quotes():
    quotes = requests.get(
        "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text.split("\n.\n") #взяли текст методом GET і розділили його по пробілу

    # MAPPING NEW QUOTES WITH CAPITAL LETTERS!!!
    quotes_capital = list(map(lambda quote: quote.upper(), quotes)) # map юзаєм в колекції

    print( {"initial": quotes, "capitalized": quotes_capital})

capital_lettered_quotes()