# 03/13 토요일

# 동적 계획법 1 - 신나는 함수 실행

import sys

memo = {}

def fun(a, b, c) :

  key = '/'.join(list(map(str, [a,b,c])))
  max_key = '20/20/20'

  if key in memo :
    return memo[key]

  elif a <= 0 or b <= 0 or c <= 0 :
    return 1

  elif a > 20 or b > 20 or c > 20 :
    if max_key not in memo :
      memo[max_key] = fun(20, 20, 20)
    return memo[max_key]

  elif a < b < c :
    memo[key] = fun(a, b, c-1) + fun(a, b-1, c-1) - fun(a, b-1, c)
    return memo[key]

  else :
    memo[key] = fun(a-1, b, c) + fun(a-1, b-1, c) + fun(a-1, b, c-1) - fun(a-1, b-1, c-1)
    return memo[key]

while True :
  a, b, c = map(int, sys.stdin.readline().split())
  if a == b == c == -1 :
    break
  print(f'w({a}, {b}, {c}) = {fun(a,b,c)}')