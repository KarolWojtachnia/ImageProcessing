import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd

org_image = plt.imread('vessel.jpeg')
bw_image = np.mean(org_image, 2)

fig, ax = plt.subplots(3, 4, figsize=(12,12))

#zadanie1
S1=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
S2=np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
S3=np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
S4=np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])

ax[0,0].imshow(nd.convolve(bw_image, S1), cmap='binary_r')
ax[0,1].imshow(nd.convolve(bw_image, S2), cmap='binary_r')
ax[0,2].imshow(nd.convolve(bw_image, S3), cmap='binary_r')
ax[0,3].imshow(nd.convolve(bw_image, S4), cmap='binary_r')

#zadanie2

def corelation(image, filter):
    x = image.shape[0]-2
    y = image.shape[1]-2
    result = np.zeros([x,y])
    for i in range(x):
        for j in range(y):
            result[i,j] = image[i,j]*filter[0,0] + image[i, j+1]*filter[0,1] + image[i, j+2]*filter[0,2] + image[i+1,j]*filter[1,0] + image[i+1, j+1]*filter[1,1] + image[i+1, j+2]*filter[1,2] + image[i+2,j]*filter[2,0] + image[i, j+1]*filter[2,1] + image[i+2, j+2]*filter[2,2]
    return result

ax[1,0].imshow(corelation(bw_image, S1), cmap='binary_r')
ax[1,1].imshow(corelation(bw_image, S2), cmap='binary_r')
ax[1,2].imshow(corelation(bw_image, S3), cmap='binary_r')
ax[1,3].imshow(corelation(bw_image, S4), cmap='binary_r')


#zadanie3
def convolution(image, filter):
    x_filter = filter.shape[0]
    y_filter = filter.shape[1]
    
    x_image = image.shape[0]
    y_image = image.shape[1]
    
    if (x_filter >  x_image):
        temp = image
        image = filter
        filter = temp

    filter = np.flip(filter, axis = 0)
    filter = np.flip(filter, axis = 1)

    x_filter = filter.shape[0]
    y_filter = filter.shape[1]
    x_image = image.shape[0]
    y_image = image.shape[1]
    
    x_result = x_image - x_filter + 1
    y_result = y_image - y_filter + 1
    result = np.zeros([x_result, y_result])
    for i in range(x_result):
        for j in range(y_result):
            sum = filter*image[i:i+x_filter, j:j+y_filter]
            sum = np.sum(sum)
            result[i,j] = sum
    return result

ax[2,0].imshow(convolution(bw_image, S1), cmap='binary_r')
ax[2,1].imshow(convolution(bw_image, S2), cmap='binary_r')
ax[2,2].imshow(convolution(bw_image, S3), cmap='binary_r')
ax[2,3].imshow(convolution(bw_image, S4), cmap='binary_r')

fig.savefig('lab5_wykres')