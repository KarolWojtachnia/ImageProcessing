import numpy as np
import matplotlib.pyplot as plt
from skimage import data

fig, ax = plt.subplots(3, 4, figsize=(12,12))

n=100
x = np.linspace(0,11*np.pi,n) 
sin = np.sin(x) 
img = sin[:, np.newaxis]*sin[np.newaxis, :]

norm = img - np.min(img)
norm = norm/np.max(norm)

bit8 = pow(2,8)-1 
norm_8bit = np.rint(norm*bit8)
ax[0,0].imshow(norm_8bit, cmap='binary_r')

fft2 = np.fft.fft2(norm_8bit)
fft2 = np.fft.fftshift(fft2)

ax[0,1].imshow(np.abs(fft2), cmap='binary_r')
ax[0,2].imshow(np.log(np.abs(fft2)), cmap='binary_r')


#zadanie 2
lin = np.linspace(0, 11*np.pi, n, dtype=int) 
x, y = np.meshgrid(lin, lin)

amp = [0, 2, 4, 6, 8, 10]
ang = [0, 1.5*np.pi, 2.4*np.pi, 3.3*np.pi, 4.1*np.pi, 5.1*np.pi]
len = [1, 2, 3, 4, 5, 6]

arr1 = np.zeros((100,100))
arr2 = np.zeros((100,100))
arr3 = np.zeros((100,100))
arr4 = np.zeros((100,100))
arr5 = np.zeros((100,100))
arr1 = amp[0]*np.sin(2*np.pi*(x*np.cos(ang[0])+y*np.sin(ang[0]))*(1/len[0]))
arr2 = amp[1]*np.sin(2*np.pi*(x*np.cos(ang[1])+y*np.sin(ang[1]))*(1/len[1]))
arr3 = amp[2]*np.sin(2*np.pi*(x*np.cos(ang[2])+y*np.sin(ang[2]))*(1/len[2]))
arr4 = amp[3]*np.sin(2*np.pi*(x*np.cos(ang[3])+y*np.sin(ang[3]))*(1/len[3]))
arr5 = amp[4]*np.sin(2*np.pi*(x*np.cos(ang[4])+y*np.sin(ang[4]))*(1/len[4]))

arr = arr1+arr2+arr3+arr4+arr5
arr_fft = np.fft.fft2(arr)
arr_fft = np.fft.fftshift(arr_fft)
arr_abs = np.abs(arr_fft)
arr_log = np.log(arr_abs)

ax[1,0].imshow(arr, cmap='binary_r')           
ax[1,1].imshow(arr_abs, cmap='binary_r')
ax[1,2].imshow(arr_log, cmap='binary_r')

camera = data.camera()

camera_fft = np.fft.fft2(camera)
camera_fft = np.fft.fftshift(camera_fft)
camera_abs = np.abs(camera_fft)
camera_log = np.log(camera_abs)

ax[2,0].imshow(camera, cmap='binary_r')           
ax[2,1].imshow(camera_abs, cmap='binary_r')
ax[2,2].imshow(camera_log, cmap='binary_r')


#zadanie 3

one_red = np.fft.ifft2(np.fft.ifftshift(fft2.real)).real
one_red = one_red - np.min(one_red)
one_red = one_red/np.max(one_red)
one_green = np.fft.ifft2(np.fft.ifftshift(fft2.imag)).real
one_green = one_green - np.min(one_green)
one_green = one_green/np.max(one_green)
one_blue = np.fft.ifft2(np.fft.ifftshift(fft2)).real
one_blue = one_blue - np.min(one_blue)
one_blue = one_blue/np.max(one_blue)
one = np.zeros([100,100,3])
one[:,:,0] = one_red
one[:,:,1] = one_green
one[:,:,2] = one_blue
print(one)
ax[0,3].imshow(one)

two_red = np.fft.ifft2(np.fft.ifftshift(arr_fft.real)).real
two_red = two_red - np.min(two_red)
two_red = two_red/np.max(two_red)
two_green = np.fft.ifft2(np.fft.ifftshift(arr_fft.imag)).real
two_green = two_green - np.min(two_green)
two_green = two_green/np.max(two_green)
two_blue = np.fft.ifft2(np.fft.ifftshift(arr_fft)).real
two_blue = two_blue - np.min(two_blue)
two_blue = two_blue/np.max(two_blue)
two = np.zeros([100,100,3])
two[:,:,0] = two_red
two[:,:,1] = two_green
two[:,:,2] = two_blue
print(two)
ax[1,3].imshow(two)

three_red = np.fft.ifft2(np.fft.ifftshift(camera_fft.real)).real
three_red = three_red - np.min(three_red)
three_red = three_red/np.max(three_red)
three_green = np.fft.ifft2(np.fft.ifftshift(camera_fft.imag)).real
three_green = three_green - np.min(three_green)
three_green = three_green/np.max(three_green)
three_blue = np.fft.ifft2(np.fft.ifftshift(camera_fft)).real
three_blue = three_blue - np.min(three_blue)
three_blue = three_blue/np.max(three_blue)
three = np.zeros([512,512,3])
three[:,:,0] = three_red
three[:,:,1] = three_green
three[:,:,2] = three_blue
print(three)
ax[2,3].imshow(three)


fig.savefig('lab6_wykres')
