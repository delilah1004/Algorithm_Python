# 03/08 월요일

# 기본 수학 2 - 소수 구하기

n, m = map(int, input().split())

num_array = [True] * (m+1)

for i in range(2, int(m**0.5)+1) :

  if num_array[i] :
    for idx in range(i+i, m+1, i) :
      num_array[idx] = False

for idx in range(n, m+1) :
  if idx!=1 and num_array[idx] :
    print(idx)