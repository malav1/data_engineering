# # Python 2 Exercises
# ​
# ## Functions
# ​
# 1. Create a function that takes two numbers as arguments and return the sum. Print the result.
# 1. Extend the above by passing an arbitrary amount of integers to a function and return the result. Print the result. Hint: use `*args`.
# 1. Pass an arbitrary amount of named arguments to a function and create a dictionary. The keys will be the names of the arguments and the values are assigned values of the named arguments. Hint: use `**kwargs`.
# 1. Create a scientific/basic calculator that makes use of separate functions to perform calculations, such as: `add`, `divide`, `area_of_a_circle` etc...
# 1. Add some form of user interface to allow the user to perform calculations
# 1. Print out a nice result / log to the screen
# ​

def add(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add(2,4,2,4,5,4))

def concatenate(**kwargs):
  return kwargs
concatenate(a=1, b=2, c=3, d=4, e=5)

def div(a,b):
    return a/b
def mul(a,b):
    return a*b

mul_or_div=input("do you want to (a)multiply or (b)divide?: ")
num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))
if mul_or_div=="a": print(f"you chose multiply. your answer is {mul(num1,num2)}")
elif mul_or_div=="b": print(f"you chose divide. your answer is {div(num1,num2)}")


# ### Bonus
# ​
# Create a fibonacci function that returns `fib(n)`. So if i request `fib(100)` it returns the 100th position in the sequence. `n` is undetermined so working out a finite sequence beforehand is not acceptable ;)
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

# ```py
# # The fibonacci sequence is the sum of the previous two values
# # 1, 1, 2, 3, 5, 8, 13...
# ​
# fib(7) # 13
# fib(50) # ?