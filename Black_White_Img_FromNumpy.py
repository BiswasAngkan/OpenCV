# Angkan Bsiwas
# 14.04.2020
# To make a black & white images from numpy matrixes

import numpy as np
import cv2

white = np.ones((512,515))				# to make a matrix having only '1'
black = np.zeros((512,512))				# to make a matrix having only '0'

concateImg = np.concatenate((white, black), axis = 1)	# to concatenate two matrices
cv2.imshow('Numpy Matrix',concateImg)			# to display the concatenate matrices
cv2.waitKey(0)						# to hold the display window until any keys pressed		
