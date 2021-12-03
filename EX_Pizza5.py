
while True:
    age = input('How old are you?''\n' 'Enter here:')
    age = int(age)

    if age <= 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket costs $10.')
    else:
        print('Your ticket costs $15.')
        
    repeat = input('Would you like to continue? (Y/N):')
    if repeat == 'N':
        break
        