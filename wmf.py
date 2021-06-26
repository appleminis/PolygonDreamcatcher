import matplotlib.pyplot as plt
import numpy as np

Ne=7
Ni=int(1e5)

rot=np.exp(2.j*np.pi/Ne)
Sn=1.j
Ss=[Sn*pow(rot,e) for e in range(Ne)]

av=0.01
Xn=np.empty(Ni,np.complex)
Xi=0.1
for i in range(Ni):
    if (np.mod(i,2)==0):#thank "think twice" hehe 
        av=np.random.randint(0,Ne)
        
    #av=4*av*(1-av)
    #av=np.mod(av,Ne)*Ne
        
    Xi = (Xi+Ss[(int(av))])*.5
    Xn[i] = Xi
    
plt.plot(np.real(Xn),np.imag(Xn),'.')
plt.show()
