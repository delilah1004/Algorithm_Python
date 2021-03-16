# 03/16 화요일

# 정수론 및 조합론 - 최소 공배수

T = int(input())

# 최소공배수 함수
def lcm(n1, n2) :
  while n2 :
    n1, n2 = n2, n1%n2
  return a*b//n2

for _ in range(T) :
  a, b = map(int, input().split())
  if b > a :
    a, b = b, a
  print(lcm(a,b))