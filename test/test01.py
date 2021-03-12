# 03/12 금요일

# 시험
# 이분 탐색 - 숫자 카드

import sys

# 상근이가 가진 숫자 카드의 개수
N = int(input())

# 상근이가 가진 숫자 카드에 적힌 정수 목록
card1 = [num for num in list(map(int, sys.stdin.readline().split()))]

card1.sort()

# 비교할 숫자 카드의 개수
M = int(input())

# 비교할 숫자 카드에 적힌 정수 목록
card2 = [num for num in list(map(int, sys.stdin.readline().split()))]

def find_card(idx) :
  left = 0
  right = N-1

  while left <= right :
    pivot = (left+right) //2
    card = card1[pivot]
    if card == card2[idx] :
      return 1
    elif card < card2[idx] :
      left = pivot + 1
    else :
      right = pivot - 1
  
  return 0

for idx in range(M) :
  print(find_card(idx), end=' ')