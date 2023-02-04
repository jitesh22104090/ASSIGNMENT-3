string="ABCDEFGHIJK "
for i in range(int(len(string)/2+1)):
    print(' '*i,string[:-(1+i*2)])