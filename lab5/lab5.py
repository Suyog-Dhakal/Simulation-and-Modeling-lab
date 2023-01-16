import matplotlib.pyplot as plt
import numpy as np

iterator = 9
G = np.zeros(shape=(iterator))
G = [35250,35500,35300,35200,33300,34500,37000,36000,35000,38500]
Y = np.zeros(shape=(iterator))
I = np.zeros(shape=(iterator))
T = np.zeros(shape=(iterator))
C = np.zeros(shape=(iterator))
Y[0] = 40000

for k in range(1,iterator):
    I[k] = 2+0.1*Y[k-1]
    Y[k] = 45.45+2.27*(I[k-1]+G[k-1])
    T[k] = 0.2*Y[k-1]
    C[k] = 20+0.7*(Y[k-1]-T[k-1])

print("Values of C:",C)
print("Values of I:",I)
print("Values of T:",T)
print("Values of Y:",Y)


fig = plt.figure()
plt.plot(Y,label="National Income(Y)")

plt.plot(C,label="Consumption(C)")

plt.plot(I,label="Investment(I)")

plt.plot(T,label="Taxes(T)")

plt.plot(G,label="Expenditure(G)")
plt.legend()
plt.show()