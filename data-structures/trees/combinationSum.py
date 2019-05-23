candidates = [10,1,2,7,6,1,5]
target = 8


def dfs(candidates, target):
    res, path = set(), ()
    if len(candidates) != 0:
        return _dfs(candidates, target, path, res)
    
def _dfs(candidates, target, path, res):
    if target == 0:
        res.add(tuple(sorted(path)))

    if target > 0:
        for i in range(len(candidates)):
            _dfs(candidates[1:], target - candidates[i], path + (candidates[i],), res)

    return res
            

candidates.sort()
print(candidates)
res = dfs(candidates, target)

print(res)
