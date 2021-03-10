# 03/10 수요일

# 스택 - 균형잡힌 세상

string_list = []

bracket = {
  ')':'(',
  ']':'['
}

while True :
  string = list(input())
  if string[-1] == '.' and len(string) == 1 :
    break
  string_list += [string]

def check_balance(string) :
  stack = []
  for s in string :
    if s in bracket.values :
      stack.append(s)
    elif s in bracket :
      if stack[-1] == bracket[s] :
        stack.pop()
      else :
        return "no"

for string in string_list :
  print(check_balance(string))