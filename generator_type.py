generator_example = (some_variable*5 for some_variable in range(1, 16))
print(generator_example)
#print(type(generator_example)) #<class 'generator'>
#print(len(generator_example)) #error "TypeError: object of type 'generator' has no len()

#Navigation through generator object
# Because generator object is iterated object, we can iterate over it. Each iteration is made calling __next__() method. Or calling next(generator_object) as
# the wrapper on the generator_object.__next__(). Because for loop always calls __next__.
print(generator_example.__next__())
print(next(generator_example)) #5, 10
print("============divider============")
for i in generator_example:
  print(i) #res : numbers from 15 to 75

#Filtering in generator expression
t = (i for i in range(1, 11) if i % 2 == 0)
print(f"t variable value is {t}")
for i in t:
  print(i)