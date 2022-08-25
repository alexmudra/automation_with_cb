#LAMBDA це спосіб оголошення ф-ії через присвоєння її змінній. Лямбда фукції - це просто такий синтаксис функції. Наприклад:

# Counting perimeter of the rectangle

rectangle_perimeter = lambda a, b: 2 * a + 2 * b #це лямбда фукція і її можна написати класичним способом

# def rectangle_perimeter (a, b):
#     return 2 * a + 2 * b


print(f"counting perimeter of sides: a=29, b=45: {rectangle_perimeter(29, 45)}") #res: counting perimeter of sides: a=29, b=45: 148
