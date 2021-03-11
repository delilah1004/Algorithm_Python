# 03/11 목요일

# 동적계획법 - 피보나치 함수

T = int(input())

# fibonacci(n) - 0의 개수
zero = {
  0: 1,
  1: 0
}

# fibonacci(n) - 1의 개수
one = {
  0: 0,
  1: 1
}

def fibonacci(n) :
  # 0 반환 횟수가 저장되어 있지 않으면
  if n not in zero :
    zero[n] = fibonacci(n-1)[0] + fibonacci(n-2)[0]
  # 1 반환 횟수가 저장되어 있지 않으면
  if n not in one :
    one[n] = fibonacci(n-1)[1] + fibonacci(n-2)[1]
  
  # 0이 반환되는 횟수와 1이 반환되는 횟수 return
  return (zero[n], one[n])

for t in range(T) :
  result = fibonacci(int(input()))
  print(f'{result[0]} {result[1]}')