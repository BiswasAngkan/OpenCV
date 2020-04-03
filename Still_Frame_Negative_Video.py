#	Angkan Biswas
#	03.05.2020
#	To make a negative video file from a squence of still file.

import os
import cv2

imgDbPath = '/home/dell/mall_dataset/frames/' 		
	
imgList = os.listdir(imgDbPath)			# os.listdir() works like 'ls' command in CLI 

n = len(imgList)
for i in range(n):
	imgPath = imgDbPath + imgList[i]
	img = cv2.imread(imgPath)
	print(i,imgPath,img.shape)

	negImg = 255-img

	cv2.imshow('Video',negImg)
	cv2.waitKey(1)
