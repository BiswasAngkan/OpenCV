# Angkan Biswas
# 07.05.2020
# To perform morphology transformation. 

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

imgPath = '/home/dell/Downloads/name.png'
imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath)

	kernel = np.ones((3,3))

	morphologyErode = cv2.erode(img, kernel)				# To shrinken foreground
	morphologyDilate = cv2.dilate(img, kernel)				# To increase the fourground
	morphologyOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)		# Opening = Erosion followed by dilation
	morphologyClose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)	# Dilation followed by erosion
	
	imgTitle = ['OrginalImage', 'MorphologyErode', 'MorphologyDilate', 'MorphologyOpening', 'MorphologyClosing'] 
	imgList = [img, morphologyErode, morphologyDilate, morphologyOpen, morphologyClose]

	for i in range(5):
		plt.subplot(2, 3, i + 1)
		plt.imshow(imgList[i], cmap = 'gray')
		plt.title(imgTitle[i])
		plt.axis('off')
	
	plt.show()
	plt.close()

else:
	print('{} does not exist'.format(imgPath))
