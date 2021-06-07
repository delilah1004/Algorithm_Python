# 03/13 토요일

# combination - N과 M

from itertools import combinations

N, M = map(int, input().split())

post = [i for i in range(1, N+1)]
com = list(combinations(post, M))

for c in com :
  print(' '.join(list(map(str, c))))