# 03/11 목요일

# DFS와 BFS - 바이러스

N = int(input())
connects = int(input())

# 컴퓨터의 연결 상태 dictionary 초기화
networks = {x:set() for x in range(1, N+1)}

# 컴퓨터의 연결 상태 저장
for c in range(1, connects+1) :
  c1, c2 = map(int, input().split())
  networks[c1].add(c2)
  networks[c2].add(c1)

# 바이러스 전파 함수
def find_virus(networks, start_node):
    queue = [start_node]
    has_virus = []
    while queue :
      current_computer = queue.pop(0)
      has_virus.append(current_computer)
      for computer in networks[current_computer] :
        # 바이러스에 감염되지 않았을 경우, 감염될 예정이 아니라면
        if computer not in has_virus and computer not in queue :
          queue.append(computer)
    # 1번 컴퓨터를 통해 바이러스에 걸린 컴퓨터의 수 반환
    return len(has_virus) - 1

# 바이러스에 걸린 컴퓨터 출력
print(find_virus(networks, 1))  # 1 이 시작노드입니다!