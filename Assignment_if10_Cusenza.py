current_users = ['mcusenza','fmagana','bmartin','iartz','mhawkins']
new_users = ['Mcusenza','Fmagana','jsmith', 'kphilipps', 'ovanloo']

for new_user in new_users:
    if new_user.lower() not in current_users:
        print('This username is available.')
    else:
        print('This username is not available, please enter a new username')
        