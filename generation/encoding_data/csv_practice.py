# Reading and writing CSV
# . Read the ford_escort.csv example file using the Python csv library and print each row.
# Remember there's a header line!
# . Extend the above so that the data is read into a dictionary.
import csv
# with open("encoding_data/car.csv") as csv_file:
#     text=csv.DictReader(csv_file, delimiter=',')
#     for line in text:
#         print(line)

# . Write the following data as CSV to a file. Add a header row with likely column titles.
data=[
    ['Joe', 'Bloggs', 40],
    ['Jane', 'Smith', 50]
    ] 
with open("encoding_data/new.csv","w+") as file:
    writer=csv.writer(file)
    writer.writerows(data)
    
with open("encoding_data/new.csv","r") as file:
    text=csv.reader(file, delimiter=",")
    for line in text:
        print(line)

# . Write another block of code that will append the following data to the file created in #3.
# ['Mike', 'Wazowski', 40] 