# 03/08 월요일

# 알고리즘 2주차 강의 - 재귀함수
# 더하거나 빼거나

array = [1,1,1,1,1]
target = 3
count = 0

def BT(array, index, result) :
  if index == len(array) :
    if result == target :
      global count 
      count += 1
    return

  num = array[index]
  BT(array, index+1, result+num, target)
  BT(array, index+1, result-num, target)

BT(array, 0, 0, target)
print(count)