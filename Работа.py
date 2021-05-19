# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:34:50 2021

@author: vias12
"""

import re
import string
import random

well=[]
bad=[]
f=open('File1.txt','w')
d=open('File2.txt','w')
N=4
count=0
uncount=0
Names=[input() for i in range(N)]
for i in Names:
    if i.isalpha()==True and i!=' ':
        if (re.findall(r'\D+', i)):
            well.append(i)
            count+=1
    else:
        bad.append(str(i))
        uncount+=1


email=[]
for i in range(count):
    g=str(Names[i])
    s=g+"@yandex.ru"
    email.append(str(s))
print(email)

        
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 12
    return ''.join(random.choice(chars) for x in range(size,20))

Passwords=[]
for i in range(count):
    Passwords.append(randompassword())
print(Passwords)



for i in range(count):
    f.write('Name: ')
    f.write(well[i]+'\n')
    f.write('Email: ')
    f.write(email[i]+'\n')
    f.write('Password: ')
    f.write(Passwords[i]+'\n')
d.write('Wrong Names:'+'\n')
for i in range(uncount):
    d.write(bad[i]+'\n')
v=open('Passwords.txt','w')

for i in range(count):
    v.write(Passwords[i]+'\n')
v.close()
f.close()
d.close()    
    
