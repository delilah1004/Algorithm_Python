# 03/09 화요일

# 재귀 - 하노이 탑 이동 순서

N = int(input())

def hanoi_count(N) :
  if N < 0 :
    return 0
  return hanoi_count(N-1) + (2**N)

print(hanoi_count(N))

stack = []
hanoi = [stack, stack, stack]

def hanoi_move(size, index) :
  global hanoi
  if index == 3 and size == hanoi[-1] -1 :
      hanoi += [size]
      return