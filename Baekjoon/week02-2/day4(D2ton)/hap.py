# 03/16 화요일

# 브루트포스 - 분해합

N = int(input())

def hap(num) :
  while num < N :
    if num < 10 :
      result = num*2
    else :
      result = num
      temp = num
      while temp > 0 :
        result += temp%10
        temp = temp//10

    if result == N :
      return num
    
    num += 1

  return 0

print(hap(1))