# Code for Calculating the sum of first N=20 odd numbers and factorial of N=8 starting from 0
# Name : Joshna Anna Sam , Roll No: 2311077

def sumodd(n):        #function to find sum of first n odd numbers
    summ=0
    i=0
    j=0
    l=[]
    while i<n:
        if j%2!=0:
            i=i+1
            l=l+[j]
            
        j=j+1
    for k in l:
        summ=summ+k
    print(l)
    return summ
        



def factorial(n):  #function to find n factorial
    fact=1
    for i in range(n+1):
        if i==0:
            fact=1
        else:
            fact=fact*i
    return fact

print("sum of firdt N=20 odd numbers:")
print(sumodd(20))
print("factorial of N=8:")
print(factorial(8))

##############################################################################################################################
#output in VS Code
#[Running] python -u "c:\Users\Admin\Documents\computationalphysicslab\#code for calculating sum of first 20 odd numbers.py"
#sum of firdt N=20 odd numbers:
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
#400
#factorial of N=8:
#40320
#[Done] exited with code=0 in 0.39 seconds
##############################################################################################################################