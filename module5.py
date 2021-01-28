f=open('mat_dv.txt','r')
l=list()
s=str()
max8=str()
max9=str()
max10=str()
max11=str()
maxal=str()
maxzr=str()
a=int(0)
b=int(0)
c=int(0)
d=int(0)
al=int(0)
zm=int(0)
for i in f:
    l=i.split(' ')
    if int(l[2])==8:
        if (int(l[3])+int(l[4])>=a):
            a=int(l[3])+int(l[4])
            max8=l[0]+' '+l[1]
    if int(l[2])==9:
        if (int(l[3])+int(l[4])>=b):
            b=int(l[3])+int(l[4])
            max9=l[0]+' '+l[1]
    if int(l[2])==10:
        if (int(l[3])+int(l[4])>=c):
            c=int(l[3])+int(l[4])
            max10=l[0]+' '+l[1]
    if int(l[2])==11:
        if (int(l[3])+int(l[4])>=d):
            d=int(l[3])+int(l[4])
            max11=l[0]+' '+l[1]
    if (int(l[3])>=al):
        al=int(l[3])
        maxal=l[0]+' '+l[1]

    if (int(l[4])>=zm):
        zm=int(l[4])
        maxzr=l[0]+' '+l[1]

print('8-',max8)
print('9-',max9)
print('10-',max10)
print('11-',max11)
print('алгебра-',maxal)
print('геометрия-',maxzr)