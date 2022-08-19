# Call with positional parameters
# Positional parameters are those which are putted by values. To which parameter bypass the value is decided by the place in the order of parameter definition in the function signature.

def average_for_three_numbers(first, second, third):
  result = (first + second + third) // 3
  return result

#named parametrs
# *Named* parameters are those which are passed by *parameter name in a signature*. In this case *name* has a value, not an order.
some2 = average_for_three_numbers(third=18, first=22, second=75)
print(some2)



some1 = average_for_three_numbers(20, 13, 26)
print(some1)

#do named paramets via dict to function
# Can be passed as a *dictionary* using notation ***dictionary_name*
average_dict = {"first": 4, "second": 5, "third": 6}
some4 = average_for_three_numbers(**average_dict) #for dict ** asterisk
print(f"the dict vatues is {average_dict}",f"and rerult of function is {some4}") #res: the dict vatues is {'first': 4, 'second': 5, 'third': 6} and rerult of function is 5


# send positional paraments via tuple to function
ght_tuple = (1, 2, 13)
some5 = average_for_three_numbers(*ght_tuple) #for tuple * asterisk
print(some5)

#Mixed way to send parametrs to argument in function
av_set = {1, 5}
av_dict = {"third": 6}

some6 = average_for_three_numbers(*av_set, **av_dict)

print(some6)
print("/////6//////")

#Send any q-ty of paramets to function - *arg

def avrg_any_params (*args):
    return sum(args) / len(args)
print(avrg_any_params(1, 5, 6, 8, 9, 45)) #do tuple with few parametrs
print(avrg_any_params(1, 5, 6, 10)) #do 2nd tuple with few parametrs
print("///////////")

#Function with any count of named parameters  - using "kvargs" (kwargs like dict)
def kvarg_func (**kwargs):
    for i in kwargs: #циклом for проходимось по ключам словника, тобто i буде присвоюватися ключ словника а не його значення
        print(f"{i} ... {kwargs[i]}")
print(kvarg_func(a=1, b=3, cisko= "normal", dom = True, f = "alex"))
print("///////////")


#Functions with mixed paratrs ("positional" and "named)
def aver_mix_param (*args, **kwargs):
    count = [*args, *(list(dict(kwargs).values()))] #do list of dict values ((list(dict(kwargs).values()))) and use their values
    return sum(count) // len(count)  #example of concatination


print(f"result of position parametrs... {aver_mix_param(1, 5, 6, 8, 9, 45)}") #result of position parametrs... 12
print(f"result of named params ... {aver_mix_param (a=1, b=3, rt = 45)}") #result of named params ... 16
print(f"result of mixed q-ty of parametrs...{aver_mix_param (10, 6, 8, first =4, second= 5)}") #result of mixed q-ty of parametrs...6
print("///////////")


#Function with named paramets and default value

def congrats_bd (name, surname, greet = "mrs."):
    print(f"My best wishes dear {greet} {name} {surname}. I with you to be a cool programmer")

congrats_bd("Alex", "Kosko") #My best wishes dear mrs. Alex Kosko. I with you to be a cool programmer
congrats_bd("Alex", "Kosko", "mister") #My best wishes dear mister Alex Kosko. I with you to be a cool programmer
