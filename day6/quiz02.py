
import sys
sys.stdin = open('a.txt','rt')

M, N = map(int, sys.stdin.readline().split())
tomato_box = []

# 토마토 초기 상태 저장
for n in range(N) :
  line = [tomato for tomato in list(map(int, sys.stdin.readline().split()))]
  tomato_box.append(line)

# print(tomato_box)

def ripe_tomato(start_tomato) :
  left_tomato = (start_tomato[0], start_tomato[1] - 1)
  right_tomato = (start_tomato[0], start_tomato[1] + 1)
  top_tomato = (start_tomato[0] - 1, start_tomato[1])
  bottom_tomato = (start_tomato[0] + 1, start_tomato[1])

  tomatos = [left_tomato, right_tomato, top_tomato, bottom_tomato]

  for tomato in tomatos :
    x, y = tomato[0], tomato[1]
    if x >= 0 and x<M and y>=0 and y<N :
      if tomato_box[x][y] == 0 :
        tomato_box[x][y] = 1


# 토마토가 익는 함수
def ripe_tomato(ripe_tomatos) :
  days = 0
  queue = ripe_tomatos
  while queue :
    temp_queue = []
    for q in queue :
      current_tomato = queue(0)
      
  # 토마토가 다 익는데 걸린 최소 날짜 반환
  return days

ripe_tomatos = [(x,y) for x in range(M) for y in range(N) if tomato_box[x][y]==1]

ripe_tomato()
