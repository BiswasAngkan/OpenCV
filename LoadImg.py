#	Angkan Biswas
#	10.04.2019
#	To display a digital image by OpenCV

import cv2

colorImg1 = cv2.imread('apple.jpg',1)		#	load an image (If image is not in the current directory write the absulate/relative path)
colorImg2=cv2.resize(colorImg1,(256,112))	#	resize the loded image when it is very large
title = 'apple'					#	name of display window
cv2.imshow(title, colorImg2)			#	display the resize image
cv2.waitKey(0)					#	hold display window until any keys press

