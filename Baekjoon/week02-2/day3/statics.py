# 03/15 월요일

# 정렬 - 통계학

import sys
from collections import Counter

N = int(input())
numbers = []

for _ in range(N) :
  numbers.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
numbers.sort()
print(numbers[N//2])

# 최빈값
count_dic = Counter(numbers)
mode_list = [k for k,v in count_dic.items() if max(count_dic.values()) == v]
if len(mode_list) > 1 :
  mode_list.remove(min(mode_list))
print(min(mode_list))

# 범위
print(max(numbers) - min(numbers))