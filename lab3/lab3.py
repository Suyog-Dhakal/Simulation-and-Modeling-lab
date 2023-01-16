import numpy as np
import matplotlib.pyplot as plt

iterator = 256
a = 29
b = 37
p = 256
n = 8
x0_2 = 0
r = np.ones(shape=(iterator))
ei = 256/n
c = np.zeros(shape=8)
r[0] = 16

for i in range(0,iterator-1):
  r[i+1] = (r[i]*a + b) % p

  if(r[i+1]<=31):
    c[0]=c[0]+1
  if (r[i+1]>31 and r[i+1]<= 63):
        c[1]=c[1]+1
  if (r[i+1]>63 and r[i+1]<= 95):
        c[2]=c[2]+1
  if (r[i+1]>95 and r[i+1]<= 127):
        c[3]=c[3]+1
  if (r[i+1]>127 and r[i+1]<= 159):
        c[4]=c[4]+1
  if (r[i+1]>159 and r[i+1]<= 191):
        c[5]=c[5]+1
  if (r[i+1]>191 and r[i+1]<= 223):
        c[6]=c[6]+1
  if (r[i+1]>223 and r[i+1]<= 255):
        c[7]=c[7]+1


for i in range(0,8):
  x0_2= x0_2 + (c[i] - ei) * (c[i] - ei) / ei

print(f"Values of r:{r}")
print(f"Values of c:{c}")
print(f"Values of x0_2:{x0_2}")

fig = plt.figure()
plt.plot(r,label='r')
plt.legend()
plt.show()