# 03/16 화요일

# 스택 - 제로

import sys
input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K) :
  num = int(input())
  if num != 0 :
    stack.append(num)
  else :
    stack.pop()

total = 0

for num in stack :
  total += num

print(total)