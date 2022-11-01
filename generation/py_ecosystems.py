from math import factorial
from factorial_func import fac
# Python Ecosystem ExercisesPython Ecosystem Exercises
# ModulesModules
# 1.  Create a Python file and import the  math  package. Use the package to print out a value using the factorial method.
# 2.  Follow the same as above but this time, only import the factorial method instead of the whole package.
print(factorial(6))
# 3.  Follow the same as above but this time, place the factorial call in a function and return the value. Create a second file that will import this function. Call the function from that module and print out the results.
print(fac(6))

# Variable ScopeVariable Scope
# 1.  Describe the scope of the variables  a ,  b ,  c  and  d  in this example:
def my_function(a):
    b = a - 2
    return b

# c = 3

# if c > 2:
d = my_function(5)
print(d)

# 2.  What is the lifetime of these variables? When will they be created and destroyed?
# 3.  Can you guess what would happen if we were to assign  c  a value of  1  instead?
# 4.  Why would this be a problem? Can you think of a way to avoid it?