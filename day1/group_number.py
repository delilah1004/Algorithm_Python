# 03/12 금요일

# 문자열 - 그룹 단어 체커

import sys

# 단어의 개수
N = int(input())

# 그룹 단어인지 체크하는 함수
def check_group(word) :
  memo = [word[0]]
  pre = word[0]
  index = 1
  while index < len(word) :
    if word[index] not in memo :
      memo.append(word[index])
    elif word[index] != pre :
      return 0
    
    pre = word[index]
    index += 1
  
  return 1

# 그룹 단어의 개수
result = 0
for i in range(N) :
  result += check_group(sys.stdin.readline())

print(result)