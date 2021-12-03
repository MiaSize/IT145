sandwich_orders = ["grilled cheese, peanut butter and jelly, ham and cheese, meatball sub, panini"]
finished_sandwiches = []

while sandwich_orders:
    orders = sandwich_orders.pop()
    print('Your order is', orders.title(), 'sandwiches.')
    finished_sandwiches.append(orders)

print('\nThe following sandwiches are done:')

for finished in finished_sandwiches:
    print(finished.title())
