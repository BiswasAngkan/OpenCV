#	Angkan Biswas
#	02.05.2019
# 	Display two images with their negatives


import cv2
import numpy

loadImg1 = cv2.imread('/home/dell/Example/apple.jpg',1)			# Load image from source folder
loadImg2 = cv2.imread('/home/dell/Example/bench.jpg',1)

positiveImg1 = cv2.resize(loadImg1,(300,200))				# Resize image
positiveImg2 = cv2.resize(loadImg2,(300,200))
				
negativeImg1 = 255 - positiveImg1					# Make negative image
negativeImg2 = 255 - positiveImg2

concateImg1 = numpy.concatenate((positiveImg1,positiveImg2),axis=1)	# Add two images	
concateImg2 = numpy.concatenate((negativeImg1,negativeImg2), axis=1)	
concateImg3 = numpy.concatenate((concateImg1,concateImg2), axis=0)

title = 'Fruits~Bench'							# Add title
cv2.imshow(title,concateImg3)						# Display image
cv2.waitKey(0)								# Show images until a key pressed
