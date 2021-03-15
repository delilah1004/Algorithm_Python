# 03/15 월요일

# 분할정복 - 쿼드 트리

import sys
input = sys.stdin.readline

N = int(input())
quad_tree = []
for _ in range(N) :
  quad_tree.append(list(map(int, list(input().strip('\n')))))

result = ''

def compress(row,col,l) :
  global result
  data = quad_tree[row][col]
  
  for r in range(row, row+l) :
    for c in range(col, col+l) :
      if quad_tree[r][c] != data :
        result += '('
        l = l//2
        compress(row, col, l)
        compress(row, col+l, l)
        compress(row+l, col, l)
        compress(row+l, col+l, l)
        result += ')'
        return 
  
  result += str(data)

compress(0,0,N)
print(result)