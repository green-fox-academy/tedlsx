from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from skimage import measure


# Set up mesh
n = 100 

x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
z = np.linspace(-3,3,n)
X, Y, Z =  np.meshgrid(x, y, z)

# Create cardioid function 
def f_heart(x,y,z):
    F = 320 * ((-x**2 * z**3 -9*y**2 * z**3/80) +
               (x**2 + 9*y**2/4 + z**2-1)**3)
    return F

# Obtain value to at every point in mesh
vol = f_heart(X,Y,Z) 

# Extract a 2D surface mesh from a 3D volume (F=0)
verts, faces = measure.marching_cubes(vol, 0, spacing=(0.1, 0.1, 0.1))


# Create a 3D figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
                cmap='Spectral', lw=1)

# Change the angle of view and title
ax.view_init(15, -15)

# ax.set_title(u"Made with ❤ (and Python)", fontsize=15) # if you have Python 3
ax.set_title("Made with <3 (and Python)", fontsize=15)

# Show me some love ^^
plt.show()