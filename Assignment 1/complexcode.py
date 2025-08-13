#Code for adding, subtracting, multiplying and finding the modulus of complex numbers
#Name: Joshna Anna Sam , Roll No: 2311077

import numpy as np
from idragonlib import*

c1=MyComplex(1.3,-2.2)
c2=MyComplex(-0.8,1.7)
c3=MyComplex(0.0,0.0)

print("\n the Two complex numbers")
c1.display_cmplx()
c2.display_cmplx()

print("\n Adding the two complex numbers")
c3.add_cmplx(c1,c2)
c3.display_cmplx()

print("\n Subtracting the two complex numbers")
c3.sub_complx(c1,c2)
c3.display_cmplx()

print("\n Multiplying the two complex numbers")
c3.mul_cmplx(c1,c2)
c3.display_cmplx()

print("\n Modulus of the two complex numbers")
mod=c1.mod_cmplx()
print(f"c1 mod = {mod:.3f}")
mod=c2.mod_cmplx()
print(f"c2 mod = {mod:.3f}")
###########################################################################################################

#Output in VS Code
#[Running] python -u "c:\Users\Admin\Documents\computationalphysicslab\complexcode.py"

#the Two complex numbers
#1.3, -2.2j
#-0.8, 1.7j

#Adding the two complex numbers
#0.5, 1.7j

#Subtracting the two complex numbers
#2.1, 0.0j

#Multiplying the two complex numbers
#-3.25, 0.8499999999999999j

#Modulus of the two complex numbers
#c1 mod = 2.255
#c2 mod = 1.542

#[Done] exited with code=0 in 0.776 seconds

##########################################################################################################
