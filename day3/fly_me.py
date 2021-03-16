# 03/12 금요일

# 기본 수학 1 - Fly me to the Alpha Centauri

import sys

T = int(input())

def count_move(left, right) :
  if right - left < 3 :
    return right - left
  else :
    count = 2
    move = 2
    left += 1
    right -= 1
    while True :
      left += move
      count += 1
      if left >= right :
        return count
      right -= move
      count += 1
      move += 1

for t in range(T) :
  x, y = map(int, sys.stdin.readline().split())
  print(count_move(x, y))
