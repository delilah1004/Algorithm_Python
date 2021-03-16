# 03/16 화요일

# 스택 - 스택

import sys
input = sys.stdin.readline

N = int(input())
stack = []

def func(order) :
  if 'push' in order :
    order, num = order.split()
    stack.append(num)
  elif 'pop' in order :
    if stack :
      print(stack.pop())
    else :
      print(-1)
  elif 'size' in order :
    print(len(stack))
  elif 'empty' in order :
    if stack :
      print(0)
    else :
      print(1)
  elif 'top' in order :
    if stack :
      print(stack[-1])
    else :
      print(-1)

for _ in range(N) :
  func(input())