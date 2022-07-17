import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
line=np.linspace(-np.pi, np.pi, 100)
x=np.cos(line)*(np.cos(line)+3)
y=np.sin(line)*(np.cos(line)+3)
z=np.sin(line)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()