# Angkan Biswas
# 15.04.2020
# To turn a clean image into a noisy image by adding pepper noise.

import cv2
from skimage.util import random_noise
import numpy as np 

imgPath = '/home/dell/Downloads/frog.jpeg'
img = cv2.imread(imgPath)

pepperImg1 = random_noise(img, mode = 'pepper', amount = 1.0)				# Extremely noisy (image will be black)
pepperImg2 = random_noise(img, mode = 'pepper', amount = 0.5)				
pepperImg3 = random_noise(img, mode = 'pepper', amount = 0.1)
pepperImg4 = random_noise(img, mode = 'pepper', amount = 0)				# No noise (orginal image)

concateImg = np.concatenate((pepperImg1,pepperImg2, pepperImg3, pepperImg4), axis = 1)

cv2.imshow('PepperyImage', concateImg)
cv2.waitKey(0)
