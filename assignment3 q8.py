Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

Set4=Set1^Set2
Set5=(Set1|Set2|Set3)-((Set1&Set2)|(Set2&Set3)|(Set1&Set3))
Set6=((Set1&Set2)|(Set2&Set3)|(Set1&Set3))-(Set1&Set2&Set3)
Set7=set()
i=1
while i <=10:
    if i not in Set1:
        Set7.add(i)
    i+=1
Set8=set()
i=1
while i <=10:
    if i not in (Set1|Set2|Set3):
        Set8.add(i)
    i+=1

print("Set of elements that are in Set1 and Set2 but not both: ", Set4)
print("Set of all elements that are in only one of the three sets Set1,Set2 and Set3: ",Set5)
print("Set of elements that are exactly two of the sets Set1, Set2 and Set3: ",Set6)
print("Set of all integers in the range 1 to 10 that are not in Set1: ", Set7)
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.", Set8)