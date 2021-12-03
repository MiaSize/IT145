
import time

def calcProd():
    product = 61
    for i in range(0,61):
        product = product - 1
        print('Tick... Tock...', product)
        time.sleep(1)
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
