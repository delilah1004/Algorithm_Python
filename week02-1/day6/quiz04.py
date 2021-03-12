# 03/11 목요일

# 동적계획법 - 가장 긴 증가하는 부분 수열

N = int(input())
array = list(map(int, input().split()))
index = 1

# index : 최대 길이
memo = {
  0: 1
}


def check_increase(index, num) :
  # 해당 숫자의 왼쪽에 위치하고 현재 숫자보다 작은 수 중 가장 큰 값
  max_num = max(a for a in array[:index] if a < num)
  
  for i in range()

  if max_num :



# 현재 인덱스에서 마지막 인덱스까지의 길이가 가장 긴 부분보다 길 때까지만
while index < N :
  check_increase(array[index])

print(max(memo.values()))