import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.transform import AffineTransform, warp
from scipy.interpolate import interp2d


#zadanie 1
#original
fig, ax = plt.subplots(4,2, figsize=(10,13))
org_chelsea = data.chelsea()
ax[0,0].imshow(org_chelsea)

#czarno bialy
chelsea = np.mean(org_chelsea, 2)
chelsea = chelsea[::8,::8]
ax[0,1].imshow(chelsea, cmap='binary_r')

#rotacja
matrix = np.zeros((3,3))
matrix[0,0] = np.cos(np.pi/12)
matrix[0,1] = -1*np.sin(np.pi/12)
matrix[1,0] = np.sin(np.pi/12)
matrix[1,1] = np.cos(np.pi/12)
matrix[2,2] = 1
transform = AffineTransform(matrix=matrix)
chelsea_rotated = warp(chelsea, transform.inverse)
ax[1,0].imshow(chelsea_rotated, cmap='binary_r')

#pochylenie
matrix = [[1,0.5,0],[0,1,0],[0,0,1]]
matrix=np.array(matrix)
# matrix = np.zeros((3,3))
# matrix[0,0] = 1
# matrix[0,1] = 0.5
# matrix[1,0] = 1
# matrix[1,1] = 1
# matrix[2,2] = 1
transform = AffineTransform(matrix=matrix)
chelsea_shifted = warp(chelsea, transform.inverse)
ax[1,1].imshow(chelsea_shifted, cmap='binary_r')


#zadanie 2
x = np.linspace(0, chelsea_rotated.shape[0]*8, chelsea_rotated.shape[0])
y = np.linspace(0, chelsea_rotated.shape[1]*8, chelsea_rotated.shape[1])
x_new = np.arange(0, chelsea_rotated.shape[0]*8, 1)
y_new = np.arange(0, chelsea_rotated.shape[1]*8, 1)
chelsea_interp2di = interp2d(y, x, chelsea_rotated,  kind='cubic')
chelsea_interp2d = chelsea_interp2di(y_new, x_new)
ax[2,0].imshow(chelsea_interp2d, cmap='binary_r')

x = np.linspace(0, chelsea_shifted.shape[0]*8, chelsea_shifted.shape[0])
y = np.linspace(0, chelsea_shifted.shape[1]*8, chelsea_shifted.shape[1])
x_new = np.arange(0, chelsea_shifted.shape[0]*8, 1)
y_new = np.arange(0, chelsea_shifted.shape[1]*8, 1)
chelsea_interp2d_2i = interp2d(y, x, chelsea_shifted,  kind='cubic')
chelsea_interp2d_2 = chelsea_interp2d_2i(y_new, x_new)
ax[2,1].imshow(chelsea_interp2d_2, cmap='binary_r')
fig.savefig('lab3_wykres')

print(chelsea_interp2d_2[:15, :15])