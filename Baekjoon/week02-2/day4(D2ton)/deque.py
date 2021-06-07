# 03/16 화요일

# 큐, 덱 - 큐 2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

def func(order) :
  global queue
  if 'push' == order[0] :
    queue.append(order[1])
  elif 'size' == order[0] :
    print(len(queue))
  elif 'empty' == order[0] :
    if queue :
      print(0)
    else :
      print(1)
  elif queue :
    if 'pop' == order[0] :
      print(queue.popleft())
    elif 'front' == order[0] :
      print(queue[0])
    elif 'back' == order[0] :
      print(queue[-1])
  else :
    print(-1)

for _ in range(N) :
  func(input().split())