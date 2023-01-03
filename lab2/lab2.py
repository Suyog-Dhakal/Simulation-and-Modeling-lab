import numpy as np
from matplotlib import pyplot as plt

a11 = -50.0
a21 = -19000.0
a22 = -21.5
ein = 1.5


def func1(v10):
  return (a11*v10 - a11*ein)

def func2(v10, v20):
  return (a21*v10 + a22*v20 - a21*ein)

if __name__ == '__main__':

  v10 = 0.0
  v20 = 0.0
  h = 0.0002
  t = np.zeros(shape=(800))
  v1 = np.zeros(shape=(800))
  v2 = np.zeros(shape=(800))

  for i in range(1,800):
    m11 = func1(v10)
    m12 = func1(v10+m11*h/2)
    m13 = func1(v10+m12*h/2)
    m14 = func1(v10+m13*h)
    v11 = v10 + ((m11 + 2*m12 + 2*m13 + m14)/6) * h

    m21 = func2(v10,v20)
    m22 = func2(v10 + h/2, v20+m21*h/2)
    m23 = func2(v10 + h/2,v20 + m22*h/2)
    m24 = func2(v10+h,v20+m23*h)
    v21 = v20 + ((m21 + 2*m22 + 2*m23 + m24)/6)*h

    v10 = v11
    v20 = v21
    t[i] = h * i
    v1[i] = v10
    v2[i] = v20
    

  plt.subplot(1,2,1)
  plt.title('v10')
  plt.plot(t,v1)

  plt.subplot(1,2,2)
  plt.title('v20')
  plt.plot(t,v2)

  plt.show()

