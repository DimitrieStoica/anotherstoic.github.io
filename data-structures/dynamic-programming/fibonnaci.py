def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)

# cache to store already calculated fibonacci values 
cache = {}
def cachedFibonacci(index):
    # check if value was already calculated
    if index in cache:
        return cache[index]
    else:
        if index <= 1:
            value = index
        else:
            value = cachedFibonacci(index-1) + cachedFibonacci(index-2)

    cache[index] = value
    return value

index = 105
for i in range(index):
    print(cachedFibonacci(i))
