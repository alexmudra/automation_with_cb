#LAMBDA це спосіб оголошення ф-ії через присвоєння її змінній. Лямбда фукції - це просто такий синтаксис функції. Наприклад:

# Counting perimeter of the rectangle

rectangle_perimeter = lambda a, b: 2 * a + 2 * b #це лямбда фукція і її можна написати класичним способом

# def rectangle_perimeter (a, b):
#     return 2 * a + 2 * b


print(f"counting perimeter of sides: a=29, b=45: {rectangle_perimeter(29, 45)}") #res: counting perimeter of sides: a=29, b=45: 148

################## RECURCION #####################

#Let's write *factorial* implementation as a recursion
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        print(
            "intermediate result for ",
            n,
            " * factorial(", n - 1, "): ",
            res
        )

        return res


print(factorial(4))

# Example of *bad recursion* (recursion loop), дефолтна глибина рекурсії в пайтоні 1000 викликів і далі буде recursion error
def bad_recursion():
  bad_recursion()

bad_recursion()