# Reading and writing JSON
# . Read the example.json handout file using the native Python json library. Print the object that is
# created
# . Print the "id" of all the items in the menu
import json

    #variable "data" stores the content that "load" generates. thats why we can reference it outside the with statement and the for loop doesn't need to be indented (unlike csv's)
with open("encoding_data/menu.json") as file:
    data= json.load(file)
for item in data['menu']['items']:
    print(item['id'])

# . Write the following data as JSON to a file.
element= { 
    'president': { 
        'name': 'Zaphod Beeblebrox', 
        'species': 'Betelgeusian' 
    } 
}

with open("encoding_data/new.json","w") as file:
    data= json.dump(element,file)
with open("encoding_data/new.json") as file1:
    data1= json.load(file1)
print(data1['president']['species'])