#	Angkan Biswas
#	02.05.2019
# Display two images horizontally


import cv2
import numpy

loadimg = cv2.imread('/home/dell/Example/apple.jpg',1) 		    # Load image from source folder
positiveimg = cv2.resize(loadimg, (300,200))				          # Resize image
negativeImg = 255 - positiveimg					                      # Make negative image
img = numpy.concatenate((positiveimg,negativeImg), axis=1)		# Add tow image
title = 'apple'							                                  # Add title
cv2.imshow(title,img)						                              # Display image
cv2.waitKey(0)                                                # Show images until a key pressed
