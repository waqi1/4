N_peo=[]
t=[]
a=10
dt=10
N_peo.append(1000)
t.append(0)
end_time=100
for i in range(int(end_time/dt)):
    m=N_peo[i]+a*N_peo[i]*dt
    N_peo.append(m)
    t.append (dt*(i+1))
    print t[-1],N_peo[-1]
import numpy as np
import matplotlib.pyplot as plt
plt.plot(t,N_peo)
plt.show()