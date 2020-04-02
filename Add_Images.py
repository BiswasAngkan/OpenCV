#	Angkan Biswas
#	02.04.2020
# 	Display two images after adition


import cv2
import numpy

loadImg1 = cv2.imread('/home/dell/Example/apple.jpg',1)			# Load image from source folder
loadImg2 = cv2.imread('/home/dell/Example/bench.jpg',1)

positiveImg1 = cv2.resize(loadImg1,(100,100))				# Resize image
positiveImg2 = cv2.resize(loadImg2,(100,100))
				
addImg = loadImg1+loadImg2

title = 'Fruits~Bench'							# Add title
cv2.imshow(title,addImg)						# Display image
cv2.waitKey(0)								# Show images until a key pressed

