from collections import Counter
import operator
from functools import reduce

def combinationSum(candidates, target):
    result = []
    output = []
    
    def bt(cs):
        if sum(cs) == target:
            p = Counter(cs)
            if p not in result:
                result.append(p)
                output.append(reduce(operator.add,[[e] * p[e] for e in p]))
            return
        elif sum(cs) > target:
            return
            
        for i in range(len(candidates)):
            cs.append(candidates[i])
            bt(cs)
            cs.pop()
            
            
    bt([])
    return output

print(combinationSum([2,3,6,7], 7))