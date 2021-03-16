# 03/16 화요일

# 정수론 및 조합론 - 이항 계수 1

from itertools import combinations

N, K = map(int, input().split())

n_list = [str(n) for n in range(1,N+1)]

print(len(list(combinations(n_list, K))))