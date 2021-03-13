# 03/13 토요일

# 동적 계획법 1 - 정수 삼각형

import sys

tri = {}

n = int(input())
for i in range(1, n+1) :
  tri[i] = list(map(int, sys.stdin.readline().split()))

max = 0

def get_max(level, index, total) :
  global max
  if level > n :
    if total > max :
      max = total
    return

  num = tri[level][index]
  total+=num
  get_max(level+1, index, total)
  get_max(level+1, index+1, total)

get_max(1, 0, 0)
print(max)