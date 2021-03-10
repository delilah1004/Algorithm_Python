# 03/10 수요일

# 스택 - 스택 수열

n = int(input())
seq = []

for i in range(n) :
  seq += [int(input())]

def check_stack() :
  stack = []
  output = []
  idx = 0

  # 1~n 까지의 숫자 스택 연산
  for i in range(1, n+1) :
    # 숫자가 수열의 현재 인덱스 값과 같다면
    if i == seq[idx] :
      output += ['+']
      output += ['-']
      idx += 1
    # 숫자가 수열의 현재 인덱스 값보다 크다면
    elif i > seq[idx] :
      return ['NO']
    # 숫자가 수열의 현재 인덱스 값보다 작다면
    else :
      stack.append(i)
      output += ['+']

    # 수열의 현재 인덱스 값과 스택의 top 값이 같으면 계속 뽑아준다.
    while stack and seq[idx] == stack[-1] :
      stack.pop()
      output += ['-']
      idx += 1

  if idx >= n-1 :
    return output
  else :
    return ['NO']
    
for o in check_stack() :
  print(o)