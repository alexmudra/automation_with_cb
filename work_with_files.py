import os

#useful links:
# https://www.w3schools.com/python/ref_func_open.asp
#https://pythonworld.ru/moduli/modul-os-path.html

#Os getcwd method To Find Current Working Directory
print(os.getcwdb()) #b'C:\\Users\\alex\\PycharmProjects\\automation_with_cb'


#format flexible path (not absolute)
pth = os.path.join("\\", "Users", "alex", "PycharmProjects", "automation_with_cb")
print(" ", pth) #\Users\alex\PycharmProjects\automation_with_cb


print("My curr dir:" , os.pardir) #..

print("Var 1:Current absolute path to project dir: ", os.path.abspath(os.path.curdir)) #Current absolute path to project dir:  C:\Users\alex\PycharmProjects\automation_with_cb
print("Var 2:", os.path.dirname(__file__)) #C:/Users/alex/PycharmProjects/automation_with_cb

print("View all files in cur dir:",os.listdir()) #return list of files

absolute_path = os.path.dirname(__file__)
print("View curr dir where the project is located:", absolute_path)


#build indepent path to file(not absolute).The file could be opened by any OS
# quotes_file = open(("C:/Users/alex/PycharmProjects/automation_with_cb", "quotes.txt"), "r")
e = os.path.normpath(os.path.dirname(__file__))
print("skdjfnkjsdf", e)

quotes_file = open("C:\Users\alex\PycharmProjects\automation_with_cb\quotes.txt", "r")
print(quotes_file)
type(quotes_file)

