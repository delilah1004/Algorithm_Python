# 최대값 찾기

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max = array[0]
    for i in array[1:] :
      if max < i :
        max = i
    return max

result = find_max_num(input)
print(result)