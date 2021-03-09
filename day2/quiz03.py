# 03/06 토요일

# 문자열 - 단어공부

from string import ascii_uppercase

alphabet_list = list(ascii_uppercase)
word = input().upper()
c = 0
dup = False
result = ''
for alphabet in alphabet_list :
  temp = word.count(alphabet)
  if c < temp :
    c = temp
    result = alphabet
    if dup :
      dup = False
  elif c == temp :
    dup = True
if dup :
  print('?')
else :
  print(result)
