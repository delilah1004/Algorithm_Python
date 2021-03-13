# 03/13 토요일

# DFS와 BFS - DFS와 BFS

import sys

N, M, V = map(int, sys.stdin.readline().split())
connect = {key:[] for key in range(1, N+1)}
dfs_visited = []

# 그래프 생성
for _ in range(M) :
  a, b = map(int, sys.stdin.readline().split())
  connect[a].append(b)
  connect[b].append(a)

# values 오름차순 정렬
for key in range(1, N+1) :
  connect[key].sort()

# 깊이 우선 탐색
def dfs(v) :
  global dfs_visited
  dfs_visited.append(v)
  for node in connect[v] :
    if node not in dfs_visited :
      dfs(node)

# 너비 우선 탐색
def bfs(v):
    queue = [v]
    visited = []
    while queue :
      node = queue.pop(0)
      visited.append(node)
      for next_node in connect[node] :
        # 방문하지 않았을 경우, 방문 예정이 아니라면
        if next_node not in visited and next_node not in queue :
          queue.append(next_node)
    # 방문 순서 리스트 반환
    return visited

dfs(V)
print(' '.join(list(map(str, dfs_visited))))
print(' '.join(list(map(str, bfs(V)))))