from random import randint


#Counting from 1 to the number which devides to 15. Note, we take range from 1 to 200
rng = range(1, 201) #do range collection
counter = 0
while (rng[counter] % 12) != 0: #logical statement
  print(f"Value of the number: {rng[counter]}. {rng[counter]} / 12 = {rng[counter] / 12}")
  counter += 1
  print(f"Counter value is {counter}")
# #result
# Value of the number: 1. 1 / 12 = 0.08333333333333333
# Counter value is 1
# Value of the number: 2. 2 / 12 = 0.16666666666666666
# Counter value is 2
# Value of the number: 3. 3 / 12 = 0.25
# Counter value is 3
# Value of the number: 4. 4 / 12 = 0.3333333333333333
# Counter value is 4
# Value of the number: 5. 5 / 12 = 0.4166666666666667
# Counter value is 5
# Value of the number: 6. 6 / 12 = 0.5
# Counter value is 6
# Value of the number: 7. 7 / 12 = 0.5833333333333334
# Counter value is 7
# Value of the number: 8. 8 / 12 = 0.6666666666666666
# Counter value is 8
# Value of the number: 9. 9 / 12 = 0.75
# Counter value is 9
# Value of the number: 10. 10 / 12 = 0.8333333333333334
# Counter value is 10
# Value of the number: 11. 11 / 12 = 0.9166666666666666
# Counter value is 11


# Usage in for loop
# Counting from 1 to 200 but interrupting the count if number is more then 15 and can be devided on 20.
for i in range(1, 200):
  if i > 15 and (i % 20) == 0:
    break
print(f"Result for break loop is {i}") #result for break loop is 20


#Usage in while loop BREAK
#Generating the pseude-random number and printing it. If number can be devided in 3, we break the loop

while True: #statement "while True" never end from loop
  num = randint(1, 100)
  print(f"Rand number: {num}")

  if (num % 3) == 0: #if devide result ==0 exit from loop
    break #stoping loop


#Keyword *continue* - stopping loop iteration
# Stops *internal* code execution and starts new iteration of the *loop*
# ##Usage in *for* loop
# Counteng from 1 to 10 and informing that number can be devided in 2.
for i in range(1, 10):
  #print(f"print range value {i}")
  if (i % 2) == 0: #chek pair if i-number is paired
    continue
  print(f"We do pring if i-number {i} is NOT devided to 2")
# #result:
# We do pring if i-number 1 is NOT devided to 2
# We do pring if i-number 3 is NOT devided to 2
# We do pring if i-number 5 is NOT devided to 2
# We do pring if i-number 7 is NOT devided to 2
# We do pring if i-number 9 is NOT devided to 2

#Check if random number is paired
rng = range(1, 11)
counter = 0

while counter < 10:
  num = rng[counter]
  print(num)
  counter += 1
  if (num % 2) == 0:
    continue
  print("It is paired...")