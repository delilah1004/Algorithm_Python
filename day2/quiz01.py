# 03/06 토요일

# 1차원 배열 - 평균은 넘겠지

case = int(input())
percent = []

for i in range(case) :
  data = list(map(int, input().split()))
  n = data[0]
  total = sum(data[1:])
  count = 0
  for grade in data[1:] :
    if grade > total/n :
      count += 1
  percent += [count/n]

for p in percent :
  print(f'{p*100:.3f}%')