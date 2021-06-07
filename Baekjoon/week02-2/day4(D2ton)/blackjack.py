# 03/16 화요일

# 브루트포스 - 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))
total = set()

def dfs(level, index, hap) :
  if level == 3 :
    if hap <= M :
      total.add(hap)
    return
  for i in range(index, N) :
    dfs(level+1, i+1, hap+cards[i])

dfs(0, 0, 0)

if M in total :
  print(M)
else :
  print(max(total))