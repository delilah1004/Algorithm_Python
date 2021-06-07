# 03/13 토요일

# 정수론 및 조합론 - 약수

import sys

N = int(input())
A_list = [a for a in list(map(int, sys.stdin.readline().split()))]

if len(A_list) == 1 :
  print(A_list[0]**2)
else :
  print(max(A_list)*min(A_list))