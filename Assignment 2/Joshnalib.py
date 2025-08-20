#CODE FOR LIBRARY
#Name: Joshna Anna Sam, Roll no: 2311077
def LCG(x=0.1,c=12345,a=1103515245,m=32768,N=1000,k=5):
    xi=x
    i=0
    number=[] #List to store randum numbers
    while i<=N:
        xi=((a*xi) + c)%m
        number.append(xi)
        i=i+1
    xis=[]
    xiks=[]
    for i in range(N-k):
        xis.append(number[i])
        xiks.append(number[i+k])
    return xis,xiks
