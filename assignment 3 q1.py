str1=str(input('enter a string'))
list1=str1.split()
list2=[]
dict1={}
dict2={}
for i in list1:
    if i not in list2:
        list2.append(i)
for i in list2:
    dict1[i]=list1.count(i)
print('for words:',dict1)
for i in str1:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
spaces=dict2.pop(' ')
print('for letters :',dict2)


