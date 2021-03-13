# 03/13 토요일

# 영화감독 숌

N = int(input())
order = N
k = 0

# k+3 자리수에서 나올 수 있는 종말의 숫자 개수 구하기
def last_num(k) :
  if k == 0 :
    return 1
  return last_num(k-1) * 8 + 10**k

# k+3 자리수 중 n번째 종말의 숫자 구하기
def get_num(n, k) :
  num = 10**(k+2)
  while n :
    num += 1
    # num이 종말의 숫자이면
    if '666' in str(num) :
      n -= 1
  return num

while True :
  # k+3 자리수에서 나올 수 있는 종말의 숫자 개수
  end_order = last_num(k)

  # 남은 영화 번호와 k+3 자리수에서 나올 수 있는 종말의 숫자 개수가 같으면
  if order == end_order :
    print(10**(k+3) - 334)
    break

  # 남은 영화 번호가 k+3 자리수에서 나올 수 있는 종말의 숫자 개수보다 작은 경우
  elif order < end_order :
    print(get_num(order, k))
    break

  order -= end_order
  k += 1