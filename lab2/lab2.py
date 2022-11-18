import numpy as np
import matplotlib.pyplot as plt

#zadanie 1
fig, ax = plt.subplots(3,3, figsize=(10,10))
x = np.linspace(0, 4*np.pi, 40)
y = np.sin(x)

ax[0,0].plot(y)


uno = y[:, np.newaxis]*y[np.newaxis, :]
ax[0,1].imshow(uno, cmap='binary')
ax[0,1].set_title('min: %.3f, max: %.3f'%(np.min(uno),np.max(uno)))

dos = uno - np.min(uno)
dos = dos/np.max(dos)
ax[0,2].imshow(dos, cmap='binary')
ax[0,2].set_title('min: %.3f, max: %.3f'%(np.min(dos),np.max(dos)))


#zadanie 2
bit2 = pow(2,2)-1
bit4 = pow(2,4)-1
bit8 = pow(2,8)-1 

ax[1,0].imshow(np.rint(dos*bit2), cmap='binary')
ax[1,0].set_title('min: %i, max: %i'%(np.min(np.rint(dos*bit2)),np.max(np.rint(dos*bit2))))
ax[1,1].imshow(np.rint(dos*bit4), cmap='binary')
ax[1,1].set_title('min: %i, max: %i'%(np.min(np.rint(dos*bit4)),np.max(np.rint(dos*bit4))))
ax[1,2].imshow(np.rint(dos*bit8), cmap='binary')
ax[1,2].set_title('min: %i, max: %i'%(np.min(np.rint(dos*bit8)),np.max(np.rint(dos*bit8))))


#zadanie 3
# WERSJA Z NUMPYem
# noise_qube = np.random.normal(size=(40,40,1000))
# noised_image = noise_qube+dos[:,:,None]
# noised_image = np.mean(noised_image, axis)
noise = np.random.normal(size=np.shape(dos))
noised = dos + noise
ax[2,0].imshow(noise, cmap='binary')
ax[2,0].set_title('noised')
noised50 = np.zeros(np.shape(dos))
noised1000 = np.zeros(np.shape(dos))
for i in range(50):
    noised50 = noised50 + dos + np.random.normal(size=np.shape(dos))
noised50_normalised = noised50 - np.min(noised50)
noised50_normalised = noised50_normalised/np.max(noised50_normalised)

for i in range(1000):
    noised1000 = noised1000 + dos + np.random.normal(size=np.shape(dos))
noised1000_normalised = noised1000 - np.min(noised1000)
noised1000_normalised = noised1000_normalised/np.max(noised1000_normalised)
ax[2,1].imshow(noised50_normalised, cmap='binary')
ax[2,1].set_title('n=50')
ax[2,2].imshow(noised1000_normalised, cmap='binary')
ax[2,2].set_title('n=1000')

fig.savefig('lab2_wykres')

