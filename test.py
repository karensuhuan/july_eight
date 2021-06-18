import string
import random
import re
list = [chr(i) for i in range(97,123)]  #大写字母+小写字母
for i in range(6):
    num = random.sample(list,10)
    str=''
    value = str.join(num) #将取出的6个随机数进行重新合并
# if not value[0].isdigit():
with open('test.txt', 'w') as f:
    for i in num:
        f.write(i + '\n')
