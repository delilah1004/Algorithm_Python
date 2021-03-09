# 정렬 - 좌표 정렬하기 2

case = int(input())

location = []

for i in range(case) :
  location += [list(map(int, input().split()))]

n = len(location)

# Bubble Sort
def bubble_sort(location) :
  global n
  for i in range(n-1) :
    for j in range(n-i-1) :
      if location[j][1] > location[j+1][1] :
        location[j], location[j+1] = location[j+1], location[j]
      elif (location[j][1] == location[j+1][1]) and (location[j][0] > location[j+1][0]) :
        location[j], location[j+1] = location[j+1], location[j]
  return

# Selection Sort
def selection_sort(location) :
  global n
  for i in range(n-1) :
    min_index = i
    for j in range(i+1,n) :
      if location[min_index][1] > location[j][1] :
        min_index = j
      elif (location[min_index][1] == location[j][1]) and (location[min_index][0] > location[j][0]) :
        min_index = j
    if min_index != i :
      location[i], location[min_index] = location[min_index], location[i]
  return

# Insertion Sort
def insertion_sort(location) :
  global n
  for i in range(1,n) :
    for j in range(i) :
      if location[i-j-1][1] > location[i-j][1] :
        location[i-j-1], location[i-j] = location[i-j], location[i-j-1]
      elif (location[i-j-1][1] == location[i-j][1]) and (location[i-j-1][0] > location[i-j][0]) :
        location[i-j-1], location[i-j] = location[i-j], location[i-j-1]
      else :
        break
  return

# Merge Sort

def merge_sort(array) :
  if len(array) == 1 :
    return array
  mid = len(array)//2
  left_array = merge_sort(array[:mid])
  right_array = merge_sort(array[mid:])
  return merge(left_array, right_array)

def merge(array1, array2) :

  merge_array = []
  array1_index = 0
  array2_index = 0

  while array1_index < len(array1) and array2_index < len(array2) :
    if array1[array1_index][1] > array2[array2_index][1] :
      merge_array += array2[array2_index]
      array2_index += 1
    elif array1[array1_index][1] == array2[array2_index][1] :
      if array1[array1_index][0] > array2[array2_index][0] :
        merge_array += array2[array2_index]
        array2_index += 1
      else :
        merge_array += array1[array1_index]
        array1_index += 1
    else :
      merge_array += array1[array1_index]
      array1_index += 1

  if array2_index > array1_index :
    merge_array += array2[array2_index:]
  else :
    merge_array += array1[array1_index:]

  return merge_array

# Python Sort

def sort(array) :
  array=[]
  n=int(input())
  for i in range(n):
      array.append(list(map(int, input().split())))
  for i in range(n):
      # a=array[i][0]
      # b=array[i][1]
      # a,b=b,a
      array[i][0],array[i][1]=array[i][1],array[i][0]
  array.sort()
  for i in range(n):
      a=array[i][0]
      b=array[i][1]
      a,b=b,a
      print(a,b)


#bubble_sort(location)
#selection_sort(location)
#insertion_sort(location)
merge_sort(location)

for l in location :
  print(l)

case = int(input())

location = []

for i in range(case) :
  X, Y = (map(int, input().split()))
  location += [Y, X]

location.sort()

for l in location :
    print(l[1], l[0])