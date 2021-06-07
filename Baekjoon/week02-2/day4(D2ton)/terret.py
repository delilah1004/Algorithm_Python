# 03/16 화요일

# 기본 수학2 - 터렛

T = int(input())
for _ in range(T) :
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  # 조규현과 백승환의 거리
  d = ((x1-x2)**2+(y1-y2)**2)**0.5
  # 위치의 개수가 무한대일 경우
  if d == 0 and r1 == r2 :
    print(-1)
  # 위치의 개수가 0인 경우
  elif d < abs(r1-r2) or d > r1+r2 :
    print(0)
  # 위치의 개수가 1인 경우
  elif d == r1+r2 or d == abs(r1-r2) :
    print(1)
  # 위치의 개수가 2인 경우
  else :
    print(2)