# 03/15 월요일

# DFS - 부분집합 구하기

# 집합
a = [1,2,3]
# 집합의 길이
n = len(a)

def dfs(level, res) :
  if level == n-1 :
    print(res)
    return
  for i in range(n) :
    dfs(level+1, res+str(a[i]))

dfs(0, "")