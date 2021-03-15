# 03/15 월요일

# 분할정복 - 색종이 만들기

import sys

N = int(input())
cp = []
result = [0, 0]

for _ in range(N) :
  cp.append(list(map(int, sys.stdin.readline().split())))

# 시작행, 마지막 행, 시작 열, 마지막 열
def divide_paper(row, col, l) :
  color = cp[row][col]

  # 색종이의 색 판별
  for r in range(row, row+l) :
    for c in range(col, col+l) :
      # 다른 경우 색종이 자르기
      if cp[r][c] != color :
        divide_paper(row, col, l//2)
        divide_paper(row, col+l//2, l//2)
        divide_paper(row+l//2, col+l//2, l//2)
        divide_paper(row+l//2, col, l//2)
        return
  
  # 색종이의 색이 모두 같은 경우
  result[color] += 1

divide_paper(0, 0, N)
print(result[0])
print(result[1])