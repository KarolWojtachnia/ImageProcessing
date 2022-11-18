from skimage.data import chelsea, moon
import numpy as np
import matplotlib.pyplot as plt

#Wczytaj obraz
D = 8
L = np.power(2, D).astype(int)
gamma3 = 3.
gamma0_3 = 0.3

def hist(image):
    hist = np.unique(image, return_counts=True)
    vhist = np.zeros((L))
    vhist[hist[0]] = hist[1] #indeksujemy po występujących wartościach i wrzucamy na te indeksy ilość ich wystąpięń
    vhist /= np.sum(vhist) #trzeba zrobić, żeeby sumowało się do 1
    vdist = np.cumsum(vhist)

    return vhist, vdist

def colour_hist(image):
    hist_red = np.unique(image[:,:,0], return_counts=True)
    hist_green = np.unique(image[:,:,1], return_counts=True)
    hist_blue = np.unique(image[:,:,2], return_counts=True)
    vhist_red, vhist_green, vhist_blue = np.zeros((3,L))
    vhist_red[hist_red[0]] = hist_red[1] #indeksujemy po występujących wartościach i wrzucamy na te indeksy ilość ich wystąpięń
    vhist_green[hist_green[0]] = hist_green[1]
    vhist_blue[hist_blue[0]] = hist_blue[1]
    vhist_red /= np.sum(vhist_red) #trzeba zrobić, żeeby sumowało się do 1
    vhist_green /= np.sum(vhist_green) #trzeba zrobić, żeeby sumowało się do 1
    vhist_blue /= np.sum(vhist_blue) #trzeba zrobić, żeeby sumowało się do 1
    return vhist_red, vhist_green, vhist_blue

fig, ax = plt.subplots(6, 3, figsize=(12,12))

lut_base = np.arange(0,L)
lut_same = np.linspace(0,255,L).astype(np.uint8)
lut_negation = np.linspace(L-1, 0, L-1).astype(int)
lut_threshold = np.linspace(0, 0, L).astype(np.uint8)
lut_threshold[50:200] = (L-1).astype(np.uint8)
lut_sinus = np.linspace(0, 2*np.pi, L)
lut_sinus = ((np.sin(lut_sinus) + 1 ) / 2) * L-1
lut_sinus = lut_sinus.astype(np.uint8)
lut_gamma0_3 = (np.linspace(255, 0, L)).astype(np.uint8)
lut_gamma0_3 = ((lut_base/(L-1)) ** (1/gamma0_3) * (L-1)).astype(np.uint8)
lut_gamma3 = np.linspace(255, 0, L).astype(np.uint8)
lut_gamma3 =  ((lut_base/(L-1)) ** (1/gamma3) * (L-1)).astype(np.uint8)

# print(lut_negation)
ax[0,0].plot(lut_same)
ax[1,0].plot(lut_negation)
ax[2,0].plot(lut_threshold)
ax[3,0].plot(lut_sinus)
ax[4,0].plot(lut_gamma0_3)
ax[5,0].plot(lut_gamma3)

raw = chelsea()
print(raw.shape)

gamma0_3image = lut_gamma0_3[raw]
gamma3image = lut_gamma3[raw]

ax[0,1].imshow(lut_same[raw])
ax[1,1].imshow(lut_negation[raw])
ax[2,1].imshow(lut_threshold[raw])
ax[3,1].imshow(lut_sinus[raw])
ax[4,1].imshow(lut_gamma0_3[raw])
ax[5,1].imshow(lut_gamma3[raw])

hist1 = colour_hist(lut_same[raw])
hist2 = colour_hist(lut_negation[raw])
hist3 = colour_hist(lut_threshold[raw])
hist4 = colour_hist(lut_sinus[raw])
hist5 = colour_hist(lut_gamma0_3[raw])
hist6 = colour_hist(lut_gamma3[raw])

print(*hist1)
ax[0,2].plot(hist1[0], c='r')
ax[0,2].plot(hist1[1], c='g')
ax[0,2].plot(hist1[2], c='b')
ax[1,2].plot(hist2[0], c='r')
ax[1,2].plot(hist2[1], c='g')
ax[1,2].plot(hist2[2], c='b')
ax[2,2].plot(hist3[0], c='r')
ax[2,2].plot(hist3[1], c='g')
ax[2,2].plot(hist3[2], c='b')
ax[3,2].plot(hist4[0], c='r')
ax[3,2].plot(hist4[1], c='g')
ax[3,2].plot(hist4[2], c='b')
ax[4,2].plot(hist5[0], c='r')
ax[4,2].plot(hist5[1], c='g')
ax[4,2].plot(hist5[2], c='b')
ax[5,2].plot(hist6[0], c='r')
ax[5,2].plot(hist6[1], c='g')
ax[5,2].plot(hist6[2], c='b')

plt.savefig('LUTOWANIE.png')



#ZADANIE 3

fig, ax = plt.subplots(2, 3, figsize=(12,12))
img_moon = moon()
moon_hist = hist(img_moon)
ax[0,0].imshow(img_moon, cmap='binary_r')
ax[0,1].plot(moon_hist[0])
ax[0,2].plot(moon_hist[1])

lut = moon_hist[1]
lut = (lut * (L-1)).astype(np.uint8)
ax[1,0].plot(lut)
ax[1,1].imshow(lut[img_moon], cmap='binary_r')
ax[1,2].plot(hist(lut[img_moon])[0])
plt.savefig('moon.png')

