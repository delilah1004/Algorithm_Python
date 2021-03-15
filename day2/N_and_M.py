# 03/13 토요일

# combination - N과 M

from itertools import combinations

N, M = map(int, input().split())

post = [i for i in range(1, N+1)]
com = list(combinations(post, M))

for c in com :
  print(' '.join(list(map(str, c))))

# 백트래킹 - N과 M

# 집합
a = [1,2,3,4,5]
# 집합의 길이
n = len(a)

N, M = map(int, input().split())
# 집합
a = [num for num in range(1, N+1)]
# 조합의 길이
num = M

print(a)

def dfs(level, start, end, res) :
  if level == num :
    print(res)
    return
  for i in range(start, end) :
    dfs(level+1, i+1, n, res+str(a[i]))

dfs(0, 0, n+1-num, "")