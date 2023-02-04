
grade=int(input("Enter grade between 4 to 10: "))
if grade==10:
    p="Outstanding"
    g="A+"
elif grade==9:
    p="Excellent"
    g="A"
elif grade==8:
    p="Very Good"
    g="B+"
elif grade==7:
    p="Good"
    g="B"
elif grade==6:
    p="Average"
    g="C+"
elif grade==5:
    p="Below Average"
    g="C"
elif grade==4:
    p="Poor"
    g="D"
else:
    print("Error")
print("Your grade is",g)
print(p, 'Performance')

