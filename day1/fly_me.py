# 03/12 금요일

# 기본 수학 1 - Fly me to the Alpha Centauri

import sys

T = int(input())

def count_move(left, right) :
  if right - left < 3 :
    return right - left
  else :
    count = 0
    move = 1
    while True :
      move += 1
      left += move
      right -= move
      count += 2
      if left == right :
        return count
      elif left > right :
        return count - 1

for t in range(T) :
  x, y = map(int, sys.stdin.readline().split())
  print(count_move(x, y))