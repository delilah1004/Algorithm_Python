# 03/16 화요일

# 백트래킹 - N과 M

N, M = map(int, input().split())
# 집합
a = [num for num in range(1, N+1)]
# 집합의 길이
n = len(a)
# 조합의 길이
num = M

def dfs(level, start, res) :
  if level == num :
    print(res)
    return
  for i in range(start, n) :
    if level == 0 :
      result = res + str(a[i])
    else :
      result = ' '.join([res, str(a[i])])
    dfs(level+1, i+1, result)

dfs(0, 0, '')