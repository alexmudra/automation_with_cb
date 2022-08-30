import random

#оголошуємо декоратор на прикладі простої фукції
def logger_func_example(func):
    def wrapper(*args, **kwargs): #назва декоратора wrapper і може бути різною
        #перевірики:
        print("=====================")
        print(f"Running function '{func.__name__}'")
        print(f"Positional arguments: {args}")
        print(f"Named parameters: {kwargs}")
        print("=====================")
        print("")

        return func(*args, **kwargs)

    return wrapper #замикання, повертається обєект wrapper


@logger_func_example
def test_two_numbers(expected, actual):
    assert expected == actual, f"Actual value '{actual}' is not equals expected: {expected}"


# @logger_func_example
# def dummy_concatenator(*args, **kwargs):
#     a = " ".join(list(map(lambda a: str(a), args)))
#     b = " ".join(list(map(lambda a: str(a), kwargs.values())))
#
#     return a + b


if __name__ == "__main__":
    import random

    a = random.randint(0, 1000)
    b = random.randint(0, 1000)

    test_two_numbers(a, a)

    print(f"Decorated function name: {dummy_concatenator.__name__}")

    print(f'{dummy_concatenator(2, True, "lala", bomb=True, emporer="Akbar", zen=False)}\n\n')

    test_two_numbers(actual=a, expected=b)

################## приклад закривання CLOSURE ################################

def count_sec_down(num: int):
    def next():
        nonlocal num # nonlocal - означає, що ми беремо перемінну із не вищої області видимості
        r = num #записуємо num в перемінну r
        num = num - 1
        return r
    return  next() #next  - це і є обєкт замикання