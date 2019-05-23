array = [3, 6, 1, 2, 4]

index = 0
for position, value in enumerate(array):
    print(index)
    if value % 2 == 0:
        tmp = array[index]
        array[index] = value
        array[position] = tmp
        index += 1
        
print(array)
