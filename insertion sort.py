L=[60,50,40,30,20,10]

for j in range(1,len(L)):

    key=L[j]
    i=j-1
    while (i>=0) and L[i]>key:
        L[i+1]=L[i]
        i=i-1
    L[i+1]=key
    
print(L)
        
