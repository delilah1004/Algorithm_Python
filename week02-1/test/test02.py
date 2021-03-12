# 03/12 금요일

# 시험
# 큐, 덱 - 카드2

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

while queue :
  if len(queue) == 1 :
    print(queue.pop())
    break
  queue.popleft()
  queue.rotate(-1)