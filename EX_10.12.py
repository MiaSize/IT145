import json

filename = 'c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//numbers.json'

fav = input("What is your favorite number?:")
print(fav)

with open(filename) as obj:
    numbers = json.load(obj)
    if numbers == fav:
       print("I know your favorite number! It's "+numbers)
    else:
        with open(filename, "w") as file:
            json.dump(fav,file)
            print("I love that number! It's been stored.")

