# Angkan Biswas
# 17.05.2020
# To perform negation & binarization on a sequence of frames of Mall Data 


import cv2
from matplotlib import pyplot as plt
import numpy as np

imgDir = '/home/dell/PythonCode/Video/Mall_Data_Frames/'
print(imgDir)

threshold = 127
maxValue = 255

plt.figure(figsize = (20,20))

for i in range(1, 2001):
	imgPath = imgDir + 'seq_00' +  str(i).zfill(4) + '.jpg'
	print(imgPath)
	loadImg = cv2.imread(imgPath)
	
	resizeImg = cv2.resize(loadImg,(280, 200))
	negativeImg = 255 - resizeImg
	grayImg = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)
	
	_, binarizeImg = cv2.threshold(grayImg, threshold, maxValue, cv2.THRESH_BINARY)	
	binarizeImg = cv2.cvtColor(binarizeImg, cv2.COLOR_GRAY2BGR)
	
	concateImg = np.concatenate((resizeImg, binarizeImg, negativeImg), axis = 1)
	print(resizeImg.shape, binarizeImg.shape)

	cv2.imshow('MallData', concateImg)
	cv2.waitKey(1)
