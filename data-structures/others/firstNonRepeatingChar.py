s = 'leetcode'

chars = [i for i in s]
res = {}

for i in chars:
    count = res.get(i)
    if count is None:
        res.update({i: 1})
    else:
        res.update({i: count + 1})

for i, j in res.items():
    if j == 1:
        print("FOUND: " + str(i))
        break
