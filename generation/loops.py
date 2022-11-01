from random import randint
# # Python 2 Exercises

# ## Loops

# 1. Print the numbers 0 to 10 using a for loop.
for x in range(0,11): print(x)

# 1. Print the numbers 0 to 10 using a while loop.
i=-1
while i<10:
    i+=1
    print(i)

# 1. Print the list of numbers below using a for loop.
py_nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
for x in py_nums: print(x)

# 1. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.
list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
for i in list1:
    for e in list2:
        if i==e: print(i)

# 1. Using a while loop, on every iteration generate a random number. If it's a multiple of 5, __break__ from the loop. If it's a multiple of 3, end the current iteration with __continue__ and print a message to show you are skipping. If it's neither, print the number and continue the loop.
#     When the loop has been broken, print a message indicating that this has happened before the program exits.

#     Hint:

#     ```py
#     import random
#     x = random.randint(1,100)
#     ```
while True:
    num=randint(1,50)
    if num%5==0:
        print("break")
        break
    elif num%3==0:
        print("this is a multiple of 3- skip")
        continue
    else: print(num)