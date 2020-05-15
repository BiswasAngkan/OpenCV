# Angkan Biswas
# 15.05.2020
# To draw boundary of available objects in an image

import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
	imgPath = '/home/dell/downloads/fish/7.Scup-porgy.jpg'
	print(imgPath)
	img = cv2.imread(imgPath)
	print(img.shape)
	
	rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	_, binaryImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
	
	boundaryLines, _ = cv2.findContours(binaryImg, 1, 2)
	n = len(boundaryLines)
	
	boundaryImg = np.zeros(rgbImg.shape, dtype = np.uint8)
	for i in range(n):
		cv2.drawContours(boundaryImg, boundaryLines, i, (255, 0, 0), 1)
	
	imgList = [img, rgbImg, grayImg, binaryImg, boundaryImg]
	title = ['BGR', 'RGB', 'GRAY', 'BINARY', 'BOUNDARY']

	subplot(imgList, title)
		
def subplot(imgList, title):
	for i in range(5):
		plt.subplot(2,3,i+1)		
		plt.title(title[i])
		plt.imshow(imgList[i], cmap ='gray')
		plt.axis('off')
	
	plt.show()
	plt.close()
		
main()
