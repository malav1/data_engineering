#  Use the below list to write all names to a file where each name is on a new line.
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"] 
# . Extend this to use try-catch.
# . Extend this to use try-catch-finally.
# . Extend this to make use of the file context manager.
# with open("files/name_list.txt","a+") as file:
#     for name in people:
#         file.write(f"{name}\n")

# . Create a text file with repeated names such as:
# John 
# James ß
# John 
# Sally 
# John 
# Sally 
# Mark 
# John 
# with open("files/jumbled_names.txt","a+") as file:
#     for name in ["john","sally","john","james","john","sally","mark"]:
#         file.write(f"{name}\n")

# Create a Python file that reads the file in. Create a dictionary where the key is the name and the value is the number of times the name appears in the text file.
dict={}
with open("files/jumbled_names.txt","r+") as file:
    names=[name.strip() for name in file.readlines()]
    for name in names:
        dict[name]=names.count(name)
print(dict)
# Write out to another file where each line looks like:
# Name: John, Count: 4
