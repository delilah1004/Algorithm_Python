# 03/08 월요일

# 기본 수학 1 - ACM 호텔

for t in range(int(input())) :
  H, W, N = map(int, input().split())

  if N%H == 0 :
    X = N//H
    Y = H
  else :
    X = N//H + 1
    Y = N%H
  print(Y*100+X)