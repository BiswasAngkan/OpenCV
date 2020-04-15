# Angkan Biswas
# 15.04.2020
# To turn a clean image into a noisy image by adding salt noise.

import cv2
from skimage.util import random_noise
import numpy as np 

imgPath = '/home/dell/Downloads/frog.jpeg'
img = cv2.imread(imgPath)

saltyImg1 = random_noise(img, mode = 'salt', amount = 1.0)				# Extremely noisy (image will be white)
saltyImg2 = random_noise(img, mode = 'salt', amount = 0.5)				
saltyImg3 = random_noise(img, mode = 'salt', amount = 0.1)
saltyImg4 = random_noise(img, mode = 'salt', amount = 0)				# No noise (orginal image)

concateImg = np.concatenate((saltyImg1,saltyImg2, saltyImg3, saltyImg4), axis = 1)

cv2.imshow('SaltyImage', concateImg)
cv2.waitKey(0)
