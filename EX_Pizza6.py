'''

#while with conditional statement version

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
'''

#active version

active = True

while active:
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
        active = False


#break version

'''
number = ''
end = ''
while number != 'quit':
    number = input('How old are you?''\n' 'Enter here:')
    number = int(number)

    if number <= 3:
        print('Your ticket is free.')
    elif number <= 12:
        print('Your ticket costs $10.')
    else:
        print('Your ticket costs $15.')

    end = input("\nIf you would like to quit, type 'quit':") 
    if end == 'quit':
        break

'''