# Angkan Biswas
# 22.04.2020
# To turn a clean image into a noisy image by adding pepper noise into two diagomnl parts & save it.

import cv2
from skimage.util import random_noise
import numpy as np

imgPath = '/home/dell/PythonCode/Picture/Me.jpeg'
img = cv2.imread(imgPath)

print(img.dtype)
img = img.astype(np.float32)								# Turn pixel range from unsigned integer into float
print(img.dtype, img.max(), img.min())
img = img / 255										# Turn pixel range from 0-255 into 0-1
print(img.dtype, img.max(), img.min())

height, width, ch = img.shape
print(height, width, ch)
h = int (height / 2)
w = int (width / 2)

x = 0; y = 0
img[y:y+h, x:x+w] = random_noise (img[y:y+h, x:x+w], mode = 'pepper', amount = 0.2)	# Add pepper noise on the top-left part
print(img[y:y+h, x:x+w].max(), img[y:y+h, x:x+w].min())
x = w; y = h
img[y:y+h, x:x+w] = random_noise (img[y:y+h, x:x+w], mode = 'pepper', amount = 0.3)	# Add pepper noise on the bottom-right part

img = 255 * img										# Turn pixel range from 0-255 into 0-1
img = img.astype(np.uint) 								# Turn pixel range from float into unsigned integer 

saveImgPath = '/home/dell/PythonCode/Picture/NoisyMe.jpeg'				
cv2.imwrite(saveImgPath, img)								# Save Picture 
