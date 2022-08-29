
def test ():
    print("start")
    for i in range(5):
        yield i #yield це подібно до return але yield буде постійно в памяті і буде ПК

a = test() #створюємо обєкт нашої фукції
print(next(a)) #передаєм а в метод next



def count_up_to(qntity):
    for i in range (qntity):
        yield i
        print(i)
    #returnt true

count_up_to(5)

#############################
#генератор списку
f = [i **2 for i in range (1, 6)]
###################
b = (i **2 for i in range (1, 6))
print(next(b))

#всередині for пройдемось по всім значенням обєкту генератора b
for i in b:
    print(i)
#####№№№№№№№№№№№№№№№№№№№№
#c = list(range (100000000000))# отримуємо помилку OverflowError: Python int too large to convert to C ssize_t, бо не використовуємо генератор
#########################
#j = [i for i in range(1000000000000)] #отримаємо memory error,  бо не використовуємо генератор
## j = (i for i in range(1000000000000))
#for i in j:
 #   print(i) # в даному випадку чере цикл for буде визивати ф-ію next і вона буде брати кожен елемент із колекції j. Ми виведем всі числа і не будемо навантажувати память

#генератор можемо перетворити в ліст
print(list(f))

#при повторному виклику генератора - отримаємо пустий список
print(list(f))


#################### ФУНКЦІЇ ГЕНЕРАТОРИ YEILD #######################

#створимо просту фукціїю
def h ():
    return [1, 2, 3, 4] #повертає список чисел

def func_gen(): #створили фукцію генератор яка повертає і
    print("start")
    for i in [5, 6, 7, 8]:
        yield i
        print("end")

#присвоїм перемінній результат роботи фцкії fun_gen
s = func_gen()
print(list(s)) #виведемо на екран результат фукції у вигляді ліста


