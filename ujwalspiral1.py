# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:06:46 2016

@author: Ankit
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib as plt

b=10
hc=100
w=0.7833
c=2673
dele=3.175e-3
Hh=80
W=0.7444
C=2773
def f(molar_flow_rates,x,param):
        tci,tci1,thi,thi1,r,R=molar_flow_rates
        b,hc,w,dele=param
        derivs=[((b*hc)/(w*c)*(r+dele/2)*(tci-thi1)),
                ((b*hc)/(w*c)*(r+dele/2)*(tci-thi1)+(b*hc)/(w*c)*(r-dele/2)*(tci-thi)),
                ((b*Hh)/(w*c)*(r-dele/2)*(tci-thi)),
                ((b*Hh)/(W*C)*(R+dele/2)*(thi-tci)),
                ((b*Hh)/(W*C)*(R-dele/2)*(thi-tci1)+(b*Hh)/(W*C)*(R+dele/2)*(thi-tci)),
                ((b*hc)/(W*C)*(R-dele/2)*(thi-tci1))]
        return derivs
                
xstop=3*3.147
xinc=0.01
x=np.arange(0.,xstop,xinc)
    

param=[b,hc,w,dele]
tci0=60
tci10=150.4
thi0=200
thi10=120        
r0=10
R0=20
molar_flow_rates0=[tci0,tci10,thi0,thi10,r0,R0]
        
psoln=odeint(f,molar_flow_rates0,x,args=(param,))
#plt.plot(molar_flow_rates[1],molar_flow_rates[4],'o')
#plt.show()
print psoln    
#heat balance
tout=200-(w*c*(90.932-60)/(W*C))
print tout