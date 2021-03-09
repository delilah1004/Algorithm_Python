# 03/08 월요일

# 기본 수학 1 - 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

day = 1
if V > A :
  day += (V-A)//(A-B)
  if ((V-A)%(A-B)) :
    day += 1

print(day)