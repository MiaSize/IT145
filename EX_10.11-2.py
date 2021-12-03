import json

filename = 'c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//numbers.json'

with open(filename) as obj:
    numbers = json.load(obj)

print("I know your favorite number! It's "+numbers)
