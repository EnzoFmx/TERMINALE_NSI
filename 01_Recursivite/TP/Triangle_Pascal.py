def coef(n,p):
    if p==0 or n == p :
        return 1
    else :
        return coef(n-1,p-1) + coef(n-1,p)
    
for i in range(3):
    for j in range(i+1):
        print(coef(i,j),' ',end='')
    print()