# 03/05 금요일

# while 문 - 더하기 사이클

origin = int(input())
start = origin
count = 1

while origin :
  temp = start//10 + start%10
  result = int(str(start%10) + str(temp%10))
  if origin == result :
    break
  count += 1
  start = result

print(count)