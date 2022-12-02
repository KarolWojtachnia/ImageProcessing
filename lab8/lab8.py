from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon
import numpy as np
import matplotlib.pyplot as plt

shepp = shepp_logan_phantom()
print(shepp.shape)
theta = np.linspace(0, 180, 100)

#ZADANIE1
fig, ax = plt.subplots(1,2, figsize=(14,7))

ax[0].imshow(shepp)
ax[1].imshow(radon(shepp, theta), aspect='auto', interpolation='nearest')

plt.savefig('lab7_wykres1')

#ZADANIE2
fig, ax = plt.subplots(1, 4, figsize=(28,7))
ax[0].imshow(shepp)
ax[1].imshow(radon(shepp, theta), aspect='auto', interpolation='nearest')
ax[2].imshow(iradon(radon(shepp, theta)))
ax[3].imshow(shepp - iradon(radon(shepp, theta)))
plt.savefig('lab7_wykres2')

#ZADANIE3
fig, ax = plt.subplots(4, 4, figsize=(12,12))
shepp = shepp[50:350, 50:350]


theta10 = np.linspace(0, 180, 10)
theta30 = np.linspace(0, 180, 30)
theta100 = np.linspace(0, 180, 100)
theta1000 = np.linspace(0, 180, 1000)

radon10 = radon(shepp, theta10)
radon30 = radon(shepp, theta30)
radon100 = radon(shepp, theta100)
radon1000 = radon(shepp, theta1000)

ax[0,0].imshow(shepp)
ax[1,0].imshow(shepp)
ax[2,0].imshow(shepp)
ax[3,0].imshow(shepp)

ax[0,1].imshow(radon10, aspect='auto', interpolation='nearest')
ax[0,2].imshow(iradon(radon10, theta10))
ax[0,3].imshow(shepp - iradon(radon10, theta10))

ax[1,1].imshow(radon30, aspect='auto', interpolation='nearest')
ax[1,2].imshow(iradon(radon30,theta30))
ax[1,3].imshow(shepp - iradon(radon30, theta30))

ax[2,1].imshow(radon100, aspect='auto', interpolation='nearest')
ax[2,2].imshow(iradon(radon100, theta100))
ax[2,3].imshow(shepp - iradon(radon100, theta100))

ax[3,1].imshow(radon1000, aspect='auto', interpolation='nearest')
ax[3,2].imshow(iradon(radon1000, theta1000))
ax[3,3].imshow(shepp - iradon(radon1000, theta1000))
plt.savefig('lab7_wykres3')