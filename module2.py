f=open('E:\Perepis.txt','r')
l=list()
s=str()
a=int(input('от 19ХХ'))
b=int(input('до 19ХХ'))
for i in f:
    l=i.split("  ")
    s=l[3]
    if a<int(s[8:])<b:
        print(i)
