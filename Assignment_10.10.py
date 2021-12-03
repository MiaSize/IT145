
def count_words(filename):

    try:
        with open(filename) as obj:
            contents = obj.read()
    except:
        msg = "sorry, the file", filename + " does not exist."
        print(msg)
    else:
        
        num_words = contents.lower().count('the')
        print("the file",filename, "has the word 'the' in it", str(num_words), "times.")

filenames = ['c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//grasshopper.txt','c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//garden.txt', 'c://Users//miart//Desktop//Python_Cusenza//Assignment_Nov10//australia.txt']
for filename in filenames:
    count_words(filename)
