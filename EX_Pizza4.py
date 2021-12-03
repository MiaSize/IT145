
toppings = ("Please enter your pizza topping, once done type 'quit'.")
toppings += ('\nEnter toppings here:')

message = ''
active = True
while active:
    message = input(toppings)
    if message == 'quit':
        active = False
        print('Ending the program...')
    else:
        print('Adding', (message))
