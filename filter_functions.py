# це фукція яка використовується для фільтрації елементів послідовності: отримує фукцію яка повертаж True/False і послідовність яку потрібно фільтрувати
# Simple usage of filter function
# Filtering quotes leaving only that, which contains word or phrase given in the input

# filter_template = """
# <table>
# <tr><th>Found with pattern '{}'</th></tr>
# {}
# <tr><td><hr><br>Found {} occurances</td></tr>
# </table>
# """
#
# import requests
#
#
# def filter_quotes(pattern: str) -> list:
#     quotes = requests.get(
#         "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text.split("\n.\n")
#
#     return list(filter(lambda quote: pattern in quote, quotes))
#
#
# from IPython.display import HTML
#
# filtered = ""
# pattern = input("What to search between the quotes? ")
#
# filtered_quotes = filter_quotes(pattern)
#
# for quote in filtered_quotes:
#     filtered += f"<tr><td>{quote}</td></tr>"
#
# display(HTML(filter_template.format(pattern, filtered, len(filtered_quotes))))

#   код не буде працювати, тому що display(HTML(filter_template.format(pattern, filtered, len(filtered_quotes))))
# NameError: name 'display' is not defined

#### 3 #### фукція яка повертає лише парні числа
def s (a):
    if a % 2 == 0:
        return a

k = filter(s, (1,2,3,4)) #додамо 15 до кожного значення із кортежа
print(list(k)) #res [16, 17, 18, 19]

#фукція яка повертає лише парні числа тільки через лямбда
l = filter(lambda x: (x % 2 == 0), (2, 3, 4, 5, 6, 10, 20, 15))
print(list(l)) #res [2, 4, 6, 10, 20]

