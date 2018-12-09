def binary_add(A,B):
    C=[]
    car=0
    for i in range(0,len(A)):
        if (A[i]+B[i]+car)%2==1:
            res=1
        else:
            res=0
        if (A[i]+B[i]+car)>=2:
            car=1
        else:
            car=0
        C.append(res)
    C.append(car)
    return C

A=[1,0,1,0,1,1,1,0]
B=[0,1,0,1,1,1,1,1]
print binary_add(A,B)
