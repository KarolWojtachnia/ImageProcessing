from skimage.data import chelsea
import numpy as np
import matplotlib.pyplot as plt

#Przygotowanie przestrzeni na ploty
fig, ax = plt.subplots(2,4,figsize=(12,12/1.618))

#Wczytaj obraz
D = 8
L = np.power(2, D).astype(int) 
raw_image = chelsea()

ax[0,0].imshow(raw_image)

#Przygotowanie transforamcji monochromatycznej
monochrome_transform = np.array([0, 1, 1])
monochrome_transform = monochrome_transform/np.sum(monochrome_transform)

#Dokonaj transformacji
mono_image = raw_image * monochrome_transform[None, None]
mono_image = np.sum(mono_image, axis = -1).astype(np.uint8) #tutaj otrzymujemy wartości zmienno przecinkowe, trzeba zamknać zbiór intensywności

ax[1,0].imshow(mono_image, cmap='binary_r')

#lets make a histogram
hist = np.unique(mono_image, return_counts=True)
print(hist)

#ponożej spróbkowanie histogramu
ax[1,1].scatter(*hist, c='black', marker='x')
# ax[-1,-1].imshow(mono_image==208) #pokazanie punktów o intensywnosci 208

#teraz wektorowa forma histogramu
vhist = np.zeros((L))
vhist[hist[0]] = hist[1] #indeksujemy po występujących wartościach i wrzucamy na te indeksy ilość ich wystąpięń
vhist /= np.sum(vhist) #trzeba zrobić, żeeby sumowało się do 1

#Pokazmy hist
ax[1,2].plot(vhist, c='black')
# ax[1,2].set_ylim(0,1) #histogram powinien być <0,1> ale tutaj będzie ledwo co widać w takim wypadku

#Teraz dystrybuanta
vdist = np.cumsum(vhist)
ax[1,3].plot(vdist, c='black')

#Zapisanie plotu (.eps to będzie skalowalne => do texowej publikacji najlepiej)
plt.savefig('foo.png')