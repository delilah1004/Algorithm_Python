# 03/15 월요일

# 그리디 알고리즘 - ATM

N = int(input())
people = list(map(int, input().split()))

people.sort()

time = 0
line = []

for person in people :
  time += person
  line.append(time)

print(sum(line))