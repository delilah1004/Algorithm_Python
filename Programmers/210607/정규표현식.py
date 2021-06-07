import re

regex = r'\d'

str = '''이다은 010-123-4567 ddeelee22@gmail.com
스파르타 02-9999-9999 sparta_coding@gmail.com
Delilah Lee 010 1234 8888 delilah@gmail.com'''

result = re.findall(regex, str)
print(" ".join(result))