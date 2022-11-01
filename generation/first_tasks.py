#PART1
    #strings

first_name= "may"
second_name= "alavi"
print(f"my name is {first_name} {second_name}")

    #integers
num_1= 2
num_2= 5
total= num_1*num_2
print(f"The product of {num_1} and {num_2} is {total}")

    #lists
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
third=people[2]
third_reverse=people[-3]
new_list=people[0:-1]
print(people[0]==people[-1])

    #input
name=input("what is your name?")
calc=input("enter the nums you want to add: ")
print(f"{calc[0]} + {calc[1]} = {int(calc[0])+int(calc[1])}")
compare=input("enter the numbers you want to compare: ")
print(f"it is {compare[0]==compare[1]} that the numbers are the same")

#PART2
usr_num=int(input("enter a number: "))
if usr_num%2==0 and usr_num%4!=0: print("this is even")
elif usr_num%4==0: print("this is a multiple of 4")
else: print("this is odd")

usr_input=int(input("enter a number: "))
if usr_input%3==0: print("fizz")
elif usr_input%5==0: print("buzz")

usr_format=input("is your temperature in f or c?: ")
usr_temp=int(input("enter the temperature: "))
if usr_format=="f": print(f"the temp in c is {(usr_temp-32)*(5/9)}")
elif usr_format=="c": print(f"the temp in f is {(usr_temp*1.8)+32}")

    #bank loan
usr_age=int(input("your age: "))
usr_salary=int(input("your salary: "))
if usr_age>30 and usr_salary>=50000: print("you can get a loan of up to £100,000")
elif usr_age>30 and usr_salary>=35000: print("you can get a loan of up to £75,000")
elif usr_age>21 and usr_salary>=21000: print("you can get a loan of up to £50,000")
else: print("youre not eligible")