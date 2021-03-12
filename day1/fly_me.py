# 03/12 금요일

# 기본 수학 1 - Fly me to the Alpha Centauri

import sys

T = int(input())

def count_move(d) :
  if d <= 2 :
    return d
  elif d <= 4 :
    return 3
  else :
    # count : 목적지까지 걸리는 이동 횟수
    # move : 이동 횟수가 같은 거리의 개수
    # sym : 이동 횟수별 최대 거리
    count, move, sym = 3, 2, 4

    while sym < d :
      sym += move
      count += 1
      if count % 2 :
        move += 1

    return count
      
for t in range(T) :
  x, y = map(int, sys.stdin.readline().split())
  d = y-x
  print(count_move(d))