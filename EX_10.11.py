import json

fav = input("What is your favorite number?:")
print(fav)

with open('c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//numbers.json', "w") as file:
    json.dump(fav,file)
