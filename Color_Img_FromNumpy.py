# Angkan Bsiwas
# 14.04.2020
# To make black, white, BGR images from numpy matrixes

import numpy as np
import cv2

h = 112
w = 112

white = np.ones((h,w,3))					# to make a matrix having only '1'
black = np.zeros((h,w,3))					# to make a matrix having only '0'

blue = np.zeros ((h,w,3))
blue[:,:,0] = 255
green = np.zeros ((h,w,3))
green[:,:,1] = 255
red = np.zeros ((h,w,3))
red[:,:,2] = 255

concateImg = np.concatenate((white, black), axis = 1)		# to concatenate two matrices
concateImg = np.concatenate((concateImg, blue), axis = 1)	# to concatenate two matrices
concateImg = np.concatenate((concateImg, green), axis = 1)	# to concatenate two matrices
concateImg = np.concatenate((concateImg, red), axis = 1)	# to concatenate two matrices

cv2.imshow('Numpy Matrix',concateImg)				# to display the concatenated matrices
cv2.waitKey(0)							# to hold the display window until any keys pressed		
