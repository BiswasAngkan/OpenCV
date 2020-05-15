# Angkan Biswas
# 15.05.2020
# To draw boundary of available objects in an image

import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
	imgPath = '/home/dell/Downloads/Figure.png'
	print(imgPath)
	img = cv2.imread(imgPath)
	print(img.shape)
	
	rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	threshold = 240
	_, binaryImg1 = cv2.threshold(grayImg, threshold, 255, cv2.THRESH_BINARY)
	_, binaryImg2 = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	boundaryImg1 = detectboundary(binaryImg1, rgbImg)
	boundaryImg2 = detectboundary(binaryImg2, rgbImg)	

	imgList = [img, rgbImg, grayImg, binaryImg1, boundaryImg1, boundaryImg2]
	title = ['BGR', 'RGB', 'GRAY', 'BINARY', 'BOUNDARY1', 'BOUNDARY2']

	subplot(imgList, title)
		
def detectboundary(binaryImg, rgbImg):
	boundaryLines, _ = cv2.findContours(binaryImg, 1, 2)
	n = len(boundaryLines)
	
	boundaryImg = rgbImg.copy()
	for i in range(n):
		cv2.drawContours(boundaryImg, boundaryLines, i, (0, 255, 255), 10)
	
	return boundaryImg

def subplot(imgList, title):
	for i in range(6):
		plt.subplot(2,3,i+1)		
		plt.title(title[i])
		plt.imshow(imgList[i], cmap ='gray')
		plt.axis('off')
	
	plt.show()
	plt.close()
		
main()
