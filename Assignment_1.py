import numpy as np
import matplotlib.pyplot as plt


def graph():
    x = np.arange(0,2*np.pi,0.1)  ## one period of sine & cosine function is 2pi, 
                                  ## start from 0, end at 2pi, stpes in 0.1
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.legend(['sin(x)', 'cos(x)'])
    plt.xlabel('x value from 0 to 2pi')

    
    plt.ylim(-2, 2)
    plt.legend(['sin(x)', 'cos(x)'])
    plt.show()

if __name__ == '__main__':
    graph()

