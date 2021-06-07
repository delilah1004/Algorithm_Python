# 03/13 토요일

# 동적 계획법 1 - 파도반 수열

import sys

memo = {
  1 : 1,
  2 : 1,
  3 : 1,
  4 : 2,
  5 : 2
}

def p(n) :
  if n not in memo :
    memo[n] = p(n-1) + p(n-5)
  return memo[n]

T = int(input())

for _ in range(T) :
  print(p(int(sys.stdin.readline())))