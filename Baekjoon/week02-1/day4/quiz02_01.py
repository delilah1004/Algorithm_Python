# 03/09 화요일

# 정렬 - 좌표 정렬하기 2

case = int(input())

location = []

for i in range(case) :
  X, Y = (map(int, input().split()))
  location += [(Y, X)]

# Python Sort
location.sort()

print(f'{l[1]} {l[0]}' for l in location)