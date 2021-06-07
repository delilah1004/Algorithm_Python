# 03/15 월요일

# 그리디 알고리즘 - 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N) :
  coin = int(input())
  if coin <= K :
    coins.append(coin)

while K > 0 :
  coin = coins.pop()
  c = K//coin
  K -= coin*c
  count += c

print(count)