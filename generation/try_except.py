# Write a small program that will purposefully throw an exception, causing your program to crash
# Update it to include exception handling with a try-except block
# Update it to print the error generated by the exception
# Add an additional code path in your application which can generate another exception of of a different type and handle it seperately if it occurs
# Add functionality to print out the stack trace for an exception to see where in code it occurs (Hint: traceback

try:
    ans=int(input("whats your fave number: "))
except Exception as e:
    print(e)

try:
    l=[1,2]
    print(l[2])
except Exception as e:
    print(e)




# def my_function(*numbers):
#   added=0
#   for i in numbers:
#     added+=i
#   return added
# print(my_function(2,4,2,5,7))

# nums=[2,4,2,5,3,5]
# total=0
# for e in nums:
#     total+=e
# print(total)