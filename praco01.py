from itertools import permutations
from itertools import combinations
data=['a','b','c',1,2,3,4,5,6,7]
result1=list(permutations(data,3))
result2=list(combinations(data,2))
print(result1)
print(result2)