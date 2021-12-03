
cats = 'c://Users//miart//Desktop//Python_Cusenza//Exercise_Nov08//cats.txt'
dogs = 'c://Users//miart//Desktop//Python_Cusenza//Exercise_Nov08//dogs.txt'

try:
    with open(cats) as file_object:
        contents = file_object.read()      
    with open(dogs) as file_object:
        content = file_object.read()   
except FileNotFoundError:
    pass
else:
    print(contents)
    print(content)
