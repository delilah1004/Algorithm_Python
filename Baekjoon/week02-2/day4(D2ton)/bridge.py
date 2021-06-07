# 03/16 화요일

# 정수론 및 조합론 - 다리 놓기


t = int(input())

def factorial(num):
    if num <= 1:
        return 1
    return factorial(num-1)*num

for i in range(t):
    n,m = map(int,input().split())
    result = factorial(m) // (factorial(n)*factorial(m-n))
    print(result)