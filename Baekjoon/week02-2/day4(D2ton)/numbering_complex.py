# 03/16 화요일

# DFS와 BFS - 단지번호붙이기

import sys
input = sys.stdin.readline

# 지도의 크기 입력
N = int(input())

# 지도 정보를 입력할 리스트 초기화
house = []

# 'house'에 지도 정보 추가
for _ in range(N) :
  house.append(list(map(int, list(input().strip('\n')))))

# 집이 있는 좌표만 담을 새로운 리스트 초기화
comp_map = []

# 'comp_map'에 집이 있는 좌표 추가
for i in range(N) :
  for j in range(N) :
    if house[i][j] == 1 :
      comp_map.append((i,j))

# 각 단지내 집의 수를 저장할 dictionary
comp_dict = {}

# 단지 저장 함수
def bfs(start, num) :
  queue = [start]
  comp_dict[num] = 0
  while queue :
    house = queue.pop()
    if house in comp_map :
      comp_map.remove(house)
      comp_dict[num] += 1
    
      x = house[0]
      y = house[1]

      # 현재 집의 위, 아래, 왼쪽, 오른쪽 집
      for neighbor in [(x, y-1),(x, y+1), (x-1, y), (x+1, y)] :
        # 해당 집이 아직 방문 전이라면
        if neighbor in comp_map :
          queue.append(neighbor)
        

# 단지 번호
num = 0

# 모든 집을 순회
while comp_map :
  # 단지 번호 증가
  num += 1
  # 해당 단지에 있는 집 찾기
  bfs(comp_map[0], num)

# 단지 개수 출력
print(max(comp_dict))

# 단지내 집의 수를 오름차순으로 정렬
counts = sorted(comp_dict.values())

# 단지내 집의 수 출력
for count in counts :
  print(count)