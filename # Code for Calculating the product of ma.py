# Code for Calculating the product of matrices
# Name : Joshna Anna Sam , Roll No: 2311077
def read_matrix(filename):
    with open(filename,'r') as f:
        matrix=[]
        for line in f:
            row=[float(num) for num in line.strip().split()]
            matrix.append(row)
    return matrix


#A=[[2,-3,1.4],[2.5,1,-2],[-0.8,0,3.1]]
#B=[[0,-1,1],[1.5,0.5,-2],[3,0,-2]]
#D=[[1],[0],[-1]]
#C=[[-2],[0.5],[1.5]]
def multiply(X,Y):
    n=len(X)
    m=len(X[0])
    p=len(Y)
    q=len(Y[0])
    P=[]
    if m!=p:
        if n==p and m==q and m==1:  # here I consider the case of dot product of vectors
            print("vector dot product")  
            summ=0
            for i in range(n):
                summ=summ+(X[i][0]*Y[i][0])
            P=summ
        else:   # in this case matrix multiplication is not defined
            print("invalid")    
    else:
        for i in range(m):
            P.append([])
            for j in range(q):
                P[i].append([])
                t=0
                for k in range(p):
                    c=X[i][k]*Y[k][j]
                    t=t+c
                P[i][j]=t
    return P

A=read_matrix('asgn0_matA')
B=read_matrix('asgn0_matB')
C=read_matrix('asgn0_vecC')
D=read_matrix('asgn0_vecD')

print("Product of A and B",multiply(A,B))
print("Product of D and C is", multiply(D,C))
print("Product of B and C is", multiply(B,C))
        
###############################################################################################################################
#output
# [Running] python -u "c:\Users\Admin\Documents\computationalphysicslab\# Code for Calculating the product of ma.py"
#Product of A and B [[-0.3000000000000007, -3.5, 5.2], [-4.5, -2.0, 4.5], [9.3, 0.8, -7.0]]
#vector dot product
#Product of D and C is -3.5
#Product of B and C is [[1.0], [-5.75], [-9.0]]
#[Done] exited with code=0 in 0.382 seconds               
##############################################################################################################################
            








