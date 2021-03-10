# 03/10 수요일

# 큐 - 회전하는 큐

from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
count = 0
index = 0

while index < M :
  if target[index] == queue[0] :
    queue.popleft()
    index += 1
  else :
    d = queue.index(target[index]) % len(queue)

    if d <= len(queue)//2 :
      # 왼쪽으로 회전
      queue.append(queue.popleft())
    else :
      # 오른쪽으로 회전
      queue.appendleft(queue.pop())

    count += 1

print(count)
