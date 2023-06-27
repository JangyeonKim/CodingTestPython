# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열

from itertools import permutations

data = ['A', 'B', 'C']

result1 = list(permutations(data,3))
print(result1)

# 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

from itertools import combinations

result2 = list(combinations(data,2))
print(result2)