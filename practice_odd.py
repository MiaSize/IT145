
def oddcount(number):
    counter = 0
    for n in range(number):
        if n % 2 != 0:
            counter += 1
    return counter

total = oddcount(7)
print(total)
