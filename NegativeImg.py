#	Angkan Biswas                                                                                                            
#	13.04.2019
#	To display a negative image by OpenCV

import cv2

colorImg1 = cv2.imread('apple.jpg',1)		#	load an image
colorImg2 = cv2.resize(colorImg1,(256,112))	#	resize the loded image
negativeImg = 255 - colorImg2 			#	negative of image
title = 'apple'					#	name of display window
cv2.imshow(title, negativeImg)			#	display the negative image
cv2.waitKey(0)					#	hold display window

