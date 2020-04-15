#	Angkan Biswas
#	15.04.2020
#	To make a noisy image.

import cv2
from skimage.util import random_noise
import numpy as np

imgPath = '/home/dell/Downloads/Football.png'
img = cv2.imread(imgPath, 0)

print(img.max(), img.min())
# To convert pixel range from 0-255 into 0.0-1.0. Without this conversion concatenation of img with noisy images will be problematic. 
img = img / 255							 	
print(img.max(), img.min())									

saltyImg = random_noise(img, mode = 'salt', amount = 0.2)
pepperyImg = random_noise(img, mode = 'pepper', amount = 0.2)
saltyPepperyImg = random_noise(img, mode = 's&p', amount = 0.2)

concateImg = np.concatenate((img, saltyImg, pepperyImg, saltyPepperyImg), axis = 1)

cv2.imshow('NoisyImage', concateImg)
cv2.waitKey(0)
