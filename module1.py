f=open('E:\Perepis.txt','r')
l=list()
s=str()
sum=int()
for i in f:
    l=i.split("  ")
    s=l[3]
    if int(s[8:])<78:
        print(l[0])
        sum+=1
print(sum)
