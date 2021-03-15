# 03/15 월요일

# DFS - 중복 순열 구하기

# 집합
a = [1,2,3]
# 집합의 길이
n = len(a)
# 순열의 길이
num = 2

def dfs(level, res) :
  if level == num :
    print(res)
    return
  for i in range(n) :
    dfs(level+1, res+str(a[i]))

dfs(0, "")
