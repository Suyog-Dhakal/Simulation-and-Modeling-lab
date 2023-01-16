'''
This code uses the StateSpace class from the signal module of the scipy library to model a damped spring system.
The spring constant (k) and mass (m) are defined as constants, and a range of damping coefficients (D) are defined in a list.
A for loop iterates through the range of damping coefficients, 
for each iteration it constructs a state space system using the StateSpace class and using the defined matrices A, B, C, E. 
Then it uses the step function from the signal module to simulate the system and get the step response of the system, 
which is a common way to analyze the dynamic behavior of a system. The step response is a plot of the system's output (displacement) versus time, 
starting from an initial condition of zero. The step function returns the time and output values in two arrays, which are then plotted. 
The plot of the step response is generated for each value of damping coefficient, and the different response are shown in different colors.
'''

import matplotlib.pyplot as plt
from scipy import signal

k = 10
m = 10
D = [4, 8, 16, 20, 40, 80]

for i in range(0,5):
    A = [[0, 1], [-k/m, -D[i]/m]]
    B = [[0], [k/m]]
    C = [1, 0]
    E = [0]
    my_ss = signal.StateSpace(A, B, C, E)
    t, y = signal.step(my_ss)
    plt.plot(t, y)

    plt.legend(['0.2', '0.4', '0.8', '1', '2', '4'])