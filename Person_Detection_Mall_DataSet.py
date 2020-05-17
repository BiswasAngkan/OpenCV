# Angkan Biswas
# 17.05.2020
# To detect persons of Mall data frames

import cv2
import numpy as np

imgDir = '/home/dell/PythonCode/Video/Mall_Data_Frames/'
print(imgDir)

def main():
	for i in range(2, 2001):
		_, previousFrame = load_image(i-1)
		bgrImg, currentFrame = load_image(i)
		
		diffImg1 = cv2.absdiff(currentFrame, previousFrame)		
		diffImg2 = cv2.cvtColor(diffImg1, cv2.COLOR_GRAY2BGR)
	
		concateImg = np.concatenate((bgrImg, diffImg2), axis = 1)
					
		cv2.imshow('MallData', concateImg)
		cv2.waitKey(1)

def load_image(i):
	imgPath = imgDir + 'seq_00' +  str(i).zfill(4) + '.jpg'
	print(imgPath)	
	loadImg = cv2.imread(imgPath)
	resizeImg = cv2.resize(loadImg,(280, 200))
	grayImg = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)
	return resizeImg, grayImg 
	

main()
