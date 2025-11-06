a=int(input())
c=0
d=len(str(a))-1
for i in range(len(str(a))):
    a1=a%10
    a=a//10
    c+=a1*10**d
    d-=1
print(c)