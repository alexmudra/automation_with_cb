import random



#OPERETIONS WITH LIST

#print list from 1 to 10
do_list_10 = [some_variable for some_variable in range (1,11)]
print(do_list_10) # res [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print list with 5*5
do_lst_5to5 = [some_variable*5 for some_variable in range(1, 10)]
print(do_lst_5to5) #res [5, 10, 15, 20, 25, 30, 35, 40, 45]


#OPERATION WITH TUPLES

#print list from 1 to 10
do_tuple_15 = tuple (some_variable for some_variable in range (1,16))
print(do_tuple_15) # res (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

#print list with 5*5
do_tuple_5to4 = tuple(some_variable*5 for some_variable in range(1, 16))
print(do_tuple_5to4) #res (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75)


#COMPREHENSIVE SET

set_10 = {num for num in range(1, 11,2)}
print(set_10) #res {1, 3, 5, 7, 9}

do_set_5to5 = {some_variable*5 for some_variable in range(1, 10,2)}
print(do_set_5to5) #res {35, 5, 45, 15, 25}


#Filtering via comprehensive expressions
nots_2 = [num for num in range(1, 15) if (num % 2) == 0]
print(nots_2) #res [2, 4, 6, 8, 10, 12, 14]


#COMPREHENSIVE ASSIGMENT FOR VARIABLES

control = random.randint(1, 21) #random number from 1 to 20
resultat = control if (control % 2) == 0 else None

print(f"Random number is {control}", f"and variables is {resultat}")