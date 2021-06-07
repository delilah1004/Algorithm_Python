# 03/16 화요일

# 동적계획법 - 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

asc_count = { 0 : 1 }
desc_count = { N-1 : 1 }
count = {}

def check_increase(index, num) :
  max_count = 0

  # 해당 숫자의 왼쪽에 위치하고 현재 숫자보다 작은 수 중 가장 큰 값
  for i in range(index) :
    if array[i] < num and asc_count[i] > max_count :
      max_count = asc_count[i]
  asc_count[index] = max_count + 1

def check_decrease(index, num) :
  max_count = 0

  # 해당 숫자의 오른쪽에 위치하고 현재 숫자보다 작은 수 중 가장 큰 값
  for i in range(N-1, index, -1) :
    if array[i] < num and desc_count[i] > max_count :
      max_count = desc_count[i]
  desc_count[index] = max_count + 1

# 현재 인덱스에서 마지막 인덱스까지의 길이가 가장 긴 부분보다 길 때까지만
if N == 1 :
  print(1)
else :
  index = 1
  while index < N :
    check_increase(index, array[index])
    check_decrease(N-index-1, array[N-index-1])
    index += 1

  for i in range(N) :
    count[i] = asc_count[i] + desc_count[i] - 1
  
  print(max(count.values()))
