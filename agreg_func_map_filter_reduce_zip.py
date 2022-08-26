#https://www.youtube.com/watch?v=UDthAJmD3EQ
import requests

# map function - приймає як параметр фукцію як обєкт
#приклад:
# def go_map (a):
#     return a**2
# some_lst = [1, 2 , 3 , 4]
# do_map = (map(go_map, some_lst))
# print(list(do_map)) #результат print(list(do_map))

###################### 2 #############################
def f (a, b):
    return a * b

lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
lst_tree = [7, 8]

use_map = map(f, lst_one, lst_two) #перемножиться кожне значення ліста1 і ліста2 по черзі
use_map = map(f, [1, 2, 3, 4], [5, 6, 7, 8]) #перемножиться кожне значення із вложених  лістів аргументів

use_map_g = map(f, lst_one, lst_tree) #перемножиться лиле 2 значення із вложених  лістів аргументів
print(f"Result of 2 numbers {list(use_map_g)}")  #Result of 2 numbers [7, 16]

print(use_map) #поверне обєкт <map object at 0x01433FB8>
print(list(use_map)) #конвертуємо перемінну в ліст і виведе результат множення відповідно до f фукції

###################### 2 #############################
#використаємо кортеж і лямбда фуцкцію
d = map(lambda x:x+15, (1,2,3,4)) #додамо 15 до кожного значення із кортежа
print(list(d)) #res [16, 17, 18, 19]

###################### 3 #############################
def capital_lettered_quotes():
    quotes = requests.get(
        "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text.split("\n.\n") #взяли текст методом GET і розділили його по пробілу

    # MAPPING NEW QUOTES WITH CAPITAL LETTERS!!!
    quotes_capital = list(map(lambda quote: quote.upper(), quotes)) # map юзаєм в колекції

    print( {"initial": quotes, "capitalized": quotes_capital})

capital_lettered_quotes()

###################### reduce function #############################
#reduce фуцкція повертає лише одне значення із послідовності яке відповідає логічній умові
from functools import reduce

j = reduce(lambda x, b: x * b, (1, 2, 3, 4, 6)) #фукція перемножила кожне число із послідовності спочатку і до кінця
print(type(j)) #res <class 'int'>
print(j) #res 144


###################### zip function #############################
#фукуція ZIP обєднує в кортежі декілька ітеруємих послідовностей
#https://www.youtube.com/watch?v=UDthAJmD3EQ

e = "abcde" #послідовність стрінга
o = [1, 2, 3, 4, 5] # послідовність набір чисел

res = zip(e, o)
print(list(res)) #форматували результат в ліст res: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
