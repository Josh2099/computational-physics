#Code for determining pi value
#Name: Joshna Anna Sam, Roll no: 2311077
import matplotlib.pyplot as plt
import Joshnalib

# determine pi
xval,yval=Joshnalib.LCG(x=0.1,c=12345,a=1103515245,m=32768,N=10005,k=5)
m=32768 #m value used

p=[]
T=[]
n=20
while n<10000: 
    points=0
    for i in range(n):
        x=xval[i]/m
        y=yval[i]/m
        if (x**2)+(y**2)<1:
                points=points+1
        i=i+1
    pival=4*(points)/(n)
    p.append(pival)
    T.append(n)
    n=n+20


plt.scatter(T,p)
plt.title("PI VALUES VS TRIALS")
plt.xlabel("N")
plt.ylabel("pi value")
plt.grid(True)
pic="PIVALUE.png"
plt.savefig(pic)
plt.show()
z=p[::-1]
def s(l):
     ans=0
     for i in l:
          ans=ans+i
     return ans
avg=(s(z[299:])/200)


print("average of last 200 values of pi=", avg)

#OUTPUT
#[Running] python -u "c:\Users\Admin\Documents\computationalphysicslab\Assignment1bpi.py"
#average of last 200 values of pi= 3.102780124297514

#[Done] exited with code=0 in 4.74 seconds





