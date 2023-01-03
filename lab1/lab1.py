import numpy as np
from matplotlib import pyplot as plt

del_t  = 0.001
initial_time = 0
final_time = 2
t = np.arange(initial_time,final_time,del_t)

temp = int(final_time/del_t)
c1 = np.zeros(temp)
c2 = np.zeros(temp)
c3 = np.zeros(temp)

c1[0] = 15
c2[0] = 8
c3[0] = 0.2

k1 = 4
k2 = 2

for i in range(temp - 1):
  c1[i+1] = c1[i] + (k2*c3[i] - k1*c1[i]*c2[i])*del_t
  c2[i+1] = c2[i] + (k2*c3[i] - k1*c1[i]*c2[i])*del_t
  c3[i+1] = c3[i] + (2*k1*c1[i] - 2*k2*c3[i])*del_t


plt.subplot(2,2,1)
plt.plot(t,c1)

plt.subplot(2,2,2)
plt.plot(t,c2)

plt.subplot(2,2,3)
plt.plot(t,c3)

plt.show()
