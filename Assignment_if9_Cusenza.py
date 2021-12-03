users = ['mcusenza','fmagana','bmartin','iartz','admin']

for user in users:
    if user != 'admin':
        print('Hi,', user, "welcome back! Thank you for logging in today.")
    else:
        print('Welcome', user, "would you like to see audit logs for today?")

if users:
    print('The users list is not empty.')
else:
    print("We need to find some users!")
