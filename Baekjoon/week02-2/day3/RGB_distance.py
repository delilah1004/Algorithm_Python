# 03/15 월요일

# 동적 계획법 1 - RGB 거리

import sys

N = int(input())

rgb = []

# i번째 집의 색깔별 페인트칠 비용 저장
for i in range(N) :
  rgb.append(list(map(int, sys.stdin.readline().split())))

# 2번집부터 N번째 집까지을 R,G,B로 칠하는 경우 드는 최소 비용
for i in range(1, N) :
  rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
  rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
  rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[N-1]))
