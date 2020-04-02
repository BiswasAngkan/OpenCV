#	Angkan Biswas
#	02.04.2020
# 	Display two images with their negatives


import cv2
import numpy

loadImg1 = cv2.imread('/home/dell/Example/apple.jpg',1)			# Load image from source folder
loadImg2 = cv2.imread('/home/dell/Example/bench.jpg',1)

positiveImg1 = cv2.resize(loadImg1,(100,100))				# Resize image
positiveImg2 = cv2.resize(loadImg2,(100,100))
				
negativeImg1 = 255 - positiveImg1					# Make negative image
negativeImg2 = 255 - positiveImg2

concateImg1 = numpy.concatenate((positiveImg1,positiveImg2),axis=1)	# Concatenate two images horizontally	
concateImg2 = numpy.concatenate((negativeImg1,negativeImg2), axis=1)	
concateImg3 = numpy.concatenate((concateImg1,concateImg2), axis=0)	# Concatenate two images vertically
concateImg4 = numpy.concatenate((concateImg3,concateImg3), axis=1)	# Concatenate two images after adding two images

print('size of concateImg4: {}'.format(concateImg4.shape))				 

title = 'Fruits~Bench'							# Add title
cv2.imshow(title,concateImg4)						# Display image
cv2.waitKey(0)								# Show images until a key pressed

