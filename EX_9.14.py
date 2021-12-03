
from random import randint

x = randint(1, 6)
y = randint(1, 10)
z = randint(1, 20)

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        self.number = 10

    def roll_die(self):
        for _ in range(10):
            dice = randint(1, self.sides)
            print("Rolling "+str(self.sides), 'sided die, roll is a',str(dice))   
        

six = Die(6)
print(six.roll_die())

ten = Die(10)
print(ten.roll_die())

twenty = Die(20)
print(twenty.roll_die())
