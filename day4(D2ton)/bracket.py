# 03/16 화요일

# 스택 - 괄호

T = int(input())

def vps(input) :
  stack = []

  for s in list(input) :
    if not stack and s == ')' :
      return 'NO'
    elif s == ')' and stack[-1] != '(' :
      return 'NO'
    elif s == ')' and stack[-1] == '(' :
      stack.pop()
    elif s == '(' :
      stack.append(s)
    
  if stack :
    return 'NO'
  else :
    return 'YES'

for i in range(T) :
  print(vps(input().strip()))