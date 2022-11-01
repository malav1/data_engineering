# # Python 2 Exercises

# ## Dictionaries

# 1. Add a new key-value pair to the below car dictionary for the colour. Print out the colour to verify it worked.
# 1. Update the value of the model in the car dictionary. Print out the new value to verify it worked.
# 1. Delete the model key-pair from the car dictionary. Print out the entire dictionary to verify it worked.
# 1. Use the `items()` function to loop through the dictionary and print each key-value pair like so:

#   ```unix
#   key: x, value: y
#   ```

#   Hint: `for key, value in x.items():`
#   Hint: You will need to cast the values to a string

#   Car dictionary:

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False
    }

car["color"]="Red"
car["model"]="Fiesta"
car.pop("model")
print(car)

