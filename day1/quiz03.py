# 03/05 금요일

# if문 - 알람 시계

a, b = input().split()
h = int(a)
m = int(b)

if (m < 45) :
  h = (h-1)%24
m = (m-45)%60

print(h, m)
