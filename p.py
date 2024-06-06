from mpl_toolkits import mplot3d
from pylab import*
import numpy as np
def f(x,y):
    return np.sin(x+y)
    x=np.linspace(-2*pi,2*pi,100)
    y=np.linspace(-2*pi,2*pi,100)
    x,y=np.meshgrid(x,y)
    z=f(x,y)
    ax=axes(projection='3d')
    ax.contour3D(x,y,z,50)
    xlabel('x-axis')
    ylabel('y-axis')
    title('3D contour')
    show()