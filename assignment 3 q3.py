list_in=input("enter space separated numbers:").split()
list_out=[]
for j in list_in:
    i=int(j)
    list_out+=[(i,(i)**2)]
print(list_out)