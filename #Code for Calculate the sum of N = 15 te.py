#Code for Calculate the sum of N = 15 terms of a GP and HP series for common difference 1.5 and common ratio 0.5 starting from t0 = 1.25.
#Name: Joshna Anna Sam , Roll No: 2311077
def sumgp(t,r,N):
    summgp=0
    a=t
    for i in range(N):
        if i==0:
            summgp=summgp+a
        else:
            a=a*0.5
            summgp=summgp+a
    return summgp

def sumhp(t,d,N):
    summhp=0
    A=1/t
    cd=d
    for i in range(N):
        if i==0:
            summhp=summhp+(t)
        else:
            c=1/(A+cd)
            summhp=summhp+c
            cd=cd+d
    return summhp


print("sum of 15 terms of GP with first term 1.25 and common ratio 0.5 is :", sumgp(1.25,0.5,15))
print("sum 15 terms of HP with first term 1.25 and common difference 1.5 is: ", sumhp(1.25,1.5,15))


###########################################################################################################################


#Output in VS Code
#[Running] python -u "c:\Users\Admin\Documents\computationalphysicslab\#Code for Calculate the sum of N = 15 te.py"
#sum of 15 terms of GP with first term 1.25 and common ratio 0.5 is : 2.4999237060546875
#sum 15 terms of HP with first term 1.25 and common difference 1.5 is:  3.012170701620779
#[Done] exited with code=0 in 0.363 seconds


##########################################################################################################################