# 03/11 목요일

# 동적계획법 - 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

# index : 최대 길이
count = {
  0 : 1
}

def check_increase(index, num) :
  max_count = 0
  # 해당 숫자의 왼쪽에 위치하고 현재 숫자보다 작은 수 중 가장 큰 값
  for i in range(index) :
    if array[i] < num and count[i] > max_count :
      max_count = count[i]
  count[index] = max_count + 1

# 현재 인덱스에서 마지막 인덱스까지의 길이가 가장 긴 부분보다 길 때까지만
if N == 1 :
  print(count[0])
else :
  index = 1
  while index < N :
    check_increase(index, array[index])
    index += 1
  print(max(count.values()))