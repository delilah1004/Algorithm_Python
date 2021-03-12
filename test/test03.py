# 03/12 금요일

# 시험
# 정렬 - 수 정렬하기 2

import sys

N = int(sys.stdin.readline())
numbers = [] 
for _ in range(N) :
  numbers.append(int(sys.stdin.readline()))

for num in sorted(numbers) :
  print(num)