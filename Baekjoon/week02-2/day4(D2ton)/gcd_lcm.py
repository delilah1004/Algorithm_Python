# 03/16 화요일

# 정수론 및 조합론 - 최대공약수와 최소 공배수

a, b = map(int, input().split())

# 최대공약수 함수
def gcd(n1, n2) :
  while n2 :
    n1, n2 = n2, n1%n2
  return n2

m = gcd(a,b)

# 최대공약수
print(m)

# 최소공배수
print(a*b//m)