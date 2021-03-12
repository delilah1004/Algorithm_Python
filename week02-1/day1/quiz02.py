# 03/05 금요일

# 사칙연산 - 곱셈

a = int(input())
b = input()

for digit in b[::-1] :
  print(a*int(digit))

print(a*int(b))