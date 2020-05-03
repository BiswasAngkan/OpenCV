# Angkan Biswas
# 03.05.2020
# To crop a loded image file and save the cropped part.

import cv2
import os

imgPath = '/home/dell/downloads/rickshaw/10.rickshaw-kimono-iStock-1127997694.jpg'
imgStatus = os.path.isfile(imgPath)

if imgStatus == True:
 
	img = cv2.imread(imgPath)
	resizeImg = cv2.resize(img, (512, 512))
	x, y, w, h = cv2.selectROI(resizeImg)
	cropImg = resizeImg[y: y+h, x: x+w]	

	cv2.imshow('CropImg', cropImg)
	cv2.waitKey(0)
	
	saveImgPath = '/home/dell/downloads/Skype/CropImg.png'
	cv2.imwrite(saveImgPath, cropImg)

else:
	print('{} does not exist'.format(imgPath))
