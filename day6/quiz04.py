# 03/11 목요일

# 동적계획법 - 가장 긴 증가하는 부분 수열

N = int(input())
array = list(map(int, input().split()))
start = 0
max_count = 0

def check_increase(pre, next, count) :
  # 기준값이 마지막 인덱스인 경우
  if pre == N-1 :
    return count
  # 비교값이 마지막 인덱스인 경우
  elif next == N-1 :
    if array[pre] < array[next] :
      return count+1
    else :
      return count
  
  # 다음 값이 증가하면
  if array[pre] < array[next] :
    return check_increase(next, next+1, count+1)
  # 다음 값이 증가하지 않으면
  else :
    return check_increase(pre, next+1, count)

# 현재 인덱스에서 마지막 인덱스까지의 길이가 가장 긴 부분보다 길 때까지만
while start < N-1 :
  count = check_increase(start, start+1, 0)
  if max_count < count :
    max_count = count
  start += 1

print(max_count+1)