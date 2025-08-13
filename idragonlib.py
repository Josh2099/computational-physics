#Code for Library file used for complex number question
#Name: Joshna Anna Sam, Roll No: 2311077

import numpy as np

class MyComplex():
    def __init__(self,real,imag=0.0):
        self.r=real
        self.i=imag
    def display_cmplx(self):
        print(self.r,", ",self.i,"j",sep="")
    def add_cmplx(self,c1,c2):
        self.r=c1.r+c2.r
        self.i=c1.i=c2.i
        return MyComplex(self)
    def sub_complx(self,c1,c2):
        self.r=c1.r-c2.r
        self.i=c1.i-c2.i
        return MyComplex(self)
    def mul_cmplx(self,c1,c2):
        self.r=c1.r*c2.r -c1.r*c2.i
        self.i=c1.i*c2.r + c1.r*c2.i
        return MyComplex(self)
    def mod_cmplx(self):
        return np.sqrt(self.r**3 + self.i**2)