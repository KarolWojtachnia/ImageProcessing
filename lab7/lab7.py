import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import skimage.draw as disk

image1 = plt.imread('image1.jpeg')
image1 = np.mean(image1, 2)

image1_fft = np.fft.fft2(image1)
image1_fft = np.log(np.abs(np.fft.fftshift(image1_fft)))
fig, ax = plt.subplots(3, 2, figsize=(12,12))

ax[0,0].imshow(image1)
ax[0,1].imshow(image1_fft)

image1_fft_normalised = image1_fft - np.min(image1_fft)
image1_fft_normalised = image1_fft_normalised/np.max(image1_fft_normalised)

image1_fft_05 = np.copy(image1_fft_normalised)
image1_fft_08 = np.copy(image1_fft_normalised)

image1_fft_05[image1_fft_normalised < 0.5] = 0
image1_fft_05[image1_fft_normalised >= 0.5] = 1
image1_fft_08[image1_fft_normalised < 0.8] = 0
image1_fft_08[image1_fft_normalised >= 0.8] = 1

ax[1,0].imshow(image1_fft_05)
ax[1,1].imshow(image1_fft_08)

dots = np.argwhere(image1_fft_08)
print(dots[0], dots[1], dots[-2], dots[-1])

zeroed = np.fft.fftshift(np.fft.fft2(image1))
zeroed[75,:] = 0
zeroed[93,:] = 0
zeroed[131,:] = 0
zeroed[149,:] = 0

zeroed_log = np.log(np.abs(zeroed))

ax[2,0].imshow(zeroed_log)

inverse = np.fft.ifft2(np.fft.ifftshift(zeroed)).real

ax[2,1].imshow(inverse)


fig.savefig('lab7_wykres1')


#ZADANIE 3
image2 = plt.imread('image2.jpg')

image2_fft = np.fft.fft2(image2)
image2_fft = np.fft.fftshift(image2_fft)
fig, ax = plt.subplots(2, 2, figsize=(12,12))
ax[0,0].imshow(image2)
ax[0,1].imshow(np.log(np.abs(image2_fft)))

image2_fft_normalised = image2_fft - np.min(image2_fft)
image2_fft_normalised = image2_fft_normalised/np.max(image2_fft_normalised)

image2_fft_05 = np.copy(image2_fft_normalised)
image2_fft_05[image2_fft_normalised < 0.6] = 0
image2_fft_05[image2_fft_normalised >= 0.6] = 1

print(np.argwhere(image2_fft_05))
# print(dots[0], dots[1], dots[2], dots[4], dots[-6], dots[-5], dots[-4], dots[-3], dots[-2], dots[-1])

rr, cc = disk.disk((174, 238), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((174, 403), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((296, 237), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((296, 403), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((106, 319), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((364, 321), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((235, 155), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((235, 485), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((175, 75), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((115, 155), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((55, 237), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((55, 237), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((290, 75), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((355, 155), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((425, 235), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((55, 400), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((115, 485), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((175, 575), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((425, 400), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((355, 475), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0

rr, cc = disk.disk((300, 575), 10, shape=image2_fft.shape)
image2_fft[rr,cc]=0



ax[1,0].imshow(np.log(np.abs(image2_fft)))

ax[1,1].imshow(np.fft.ifft2(np.fft.ifftshift(image2_fft)).real)

fig.savefig('lab7_wykres2')