score=['小徐',5,9,6,8,7,10,6]
print(max(score[1:]))

print(min(score[1:]))

c=sorted(score[1:],reverse=True)
d=c[0:3]

e=c[4:8]
print(e)

a=sum(score[1:])
b=len(score[1:])
print(int(a/b))
####################################
for x in range(1,10):
    for y in range(1,10):
        print('%ix%i=%2i' % (x, y, y*y), end=' ')
    print()
####################################

import random
d=random.randint(1,100)
s=str(" So"*d)
a="I love so much"
for y in a :
    if  y=="s":
         c =a.replace("so",s)
"".join(c.split())
print(c)