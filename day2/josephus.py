# 03/13 토요일

# 요세푸스 순열

from collections import deque

N, K = map(int, input().split())

table = deque([str(i) for i in range(1, N+1)])
y_array = []

while table :
  table.rotate(-(K-1))
  y_array.append(table.popleft())

print("<",", ".join(y_array),">",sep='')
