# 03/06 토요일

# 문자열 - 크로아티아 알파벳

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for cro in cro_alpha :
  word = word.replace(cro, ' ')

print(len(word))