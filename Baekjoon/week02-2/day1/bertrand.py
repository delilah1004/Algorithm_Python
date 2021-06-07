# 03/12 금요일

# 기본 수학 2 - 베르트랑 공준

import sys

def prime_count(n, m) :
  num_array = [True] * (m+1)

  for i in range(2, int(m**0.5)+1) :

    if num_array[i] :
      for idx in range(i+i, m+1, i) :
        num_array[idx] = False

  print(num_array[n+1: m+1].count(True))

while True :
  n = int(sys.stdin.readline())
  if n == 0 :
    break
  prime_count(n, 2*n)