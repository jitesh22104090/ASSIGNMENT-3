n=int(input('enter number of terms in fibonacci sequence: '))
n1=0
n2=1
sumn=1
if n==1:
    print(0)
elif n==2:
    print(0,"\n1")
elif n>2:
    print(n1)
    print(n2)
    for i in range(n-2):
        n3=n1+n2
        print(n3)
        sumn+=n3
        n1=n2
        n2=n3
    print('average of fibonacci series',sum/n)
else:
    print("ERROR")