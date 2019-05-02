#	Angkan Biswas
#	01.05.2019
#	Image show side by side


import cv2
import numpy

img1 = cv2.imread('/home/dell/Example/apple.jpg',1) 		# Load image from source folder
img2 = cv2.resize(img1, (300,200))				# Resize image
negativeImg = 255 - img2					# Make negative image
img3 = numpy.concatenate((img2,negativeImg))			# Add tow image
title = 'apple'							# Add title
cv2.imshow(title,img3)						# Display image
cv2.waitKey(0)
