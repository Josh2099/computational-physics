#Code for making random number generator, basic and LCG
#Name:Joshna Anna Sam, Roll no: 2311077
import matplotlib.pyplot as plt

#Basic random number generator
def RNONE(x,c,N,P,k):
    xi=x #x0
    numbers=[] #list for storing random number
    i=0
    while i<=N:
        xi=c*xi*(1-xi)
        numbers.append(xi)
        i=i+1
    xis=[]
    xiks=[]
    for i in range(N-k):
        xis.append(numbers[i])
        xiks.append(numbers[i+k])
    y="CORRELATION PLOT for c="+str(c)+" and k="+str(k)
    #plotting
    plt.plot(xis,xiks,marker='o',linestyle='')
    plt.title(y)
    plt.xlabel("xi")
    plt.ylabel("xi+k")
    plt.grid(True)
    x="c"+str(c)+"k"+str(k)+".png"
    plt.savefig(x)
    plt.show()

#function for LCG
def LCG(x,c,a,m,N,k):
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
    y="CORRELATION PLOT for c="+str(c)+" a="+str(a)+" and k="+str(k)
    plt.plot(xis,xiks,marker='o',linestyle='')
    plt.title(y)
    plt.xlabel("xi")
    plt.ylabel("xi+k")
    plt.grid(True)
    plt.savefig("LCG.png")
    plt.show()




#question 1
RNONE(0.1,3.67,1000,1000,5)
RNONE(0.1,3.2,1000,1000,7)
RNONE(0.1,3.78,1000,1000,5)
RNONE(0.1,3.78,1000,1000,10)
RNONE(0.1,3.68,1000,1000,5)
RNONE(0.1,3.84,1000,1000,5)
RNONE(0.1,3.67,1000,1000,5)
RNONE(0.1,3.98,1000,1000,5)




#question 2

LCG(0.1,12345,1103515245,32768,1000,5)


#OUTPUT
#plots attached in Google Classroom


        

