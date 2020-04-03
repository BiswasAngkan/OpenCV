#	Angkan Biswas
#	03.05.2019
#	To make a video file from a squence of still file.

import os
import cv2

imgDbPath = '/home/dell/mall_dataset/frames/' 		
	
imgList = os.listdir(imgDbPath)			# os.listdir() works like 'ls' command in CLI 

n = len(imgList)
for i in range(n):
	imgPath = imgDbPath + imgList[i]
	img = cv2.imread(imgPath)
	print(i,imgPath,img.shape)

	cv2.imshow('Video',img)
	cv2.waitKey(1)
