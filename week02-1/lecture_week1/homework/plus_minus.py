# 03/08 월요일

# 알고리즘 2주차 강의 - 재귀함수
# 더하거나 빼거나

array = [1,1,1,1,1]
target = 3
count = 0

def plus_minus(index, result) :
  if index == len(array) :
    if result == target :
      global count 
      count += 1
    return

  num = array[index]
  plus_minus(index+1, result+num)
  plus_minus(index+1, result-num)

plus_minus(0, 0)
print(count)