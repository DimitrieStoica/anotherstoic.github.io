s = "aallcc"

charList = [i for i in s]

myDict = {}
for i,char in enumerate(s):
    myDict[char] = i

left, right = 0, 0
res = []

print(myDict)
for i,char in enumerate(s):
    right = max(right, myDict[char])

    if i == right:
        #reached the right most index
        res.append(right - left + 1)
        left = right + 1

print(res)
