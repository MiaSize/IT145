sandwich_orders = ["grilled cheese", 'peanut butter and jelly', 'ham and cheese', 'meatball', 'panini', 
'pastrami' , 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli is currently out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    orders = sandwich_orders.pop()
    print('Your order is a', orders.title(), 'sandwich.')
    finished_sandwiches.append(orders)


print('\nThe following sandwiches are done:')

for finished in finished_sandwiches:
    print(finished.title())
