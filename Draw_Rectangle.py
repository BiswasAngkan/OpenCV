# Angkan Bsiwas
# 16.04. 2020
# To draw rectangles using OpenCV's 'rectangle' function.

import cv2
import numpy as np

canvas = np.zeros((512, 512, 3))

#	cv2.rectangle(canvas, (startPointX, startPointY), (endPointX, endPointY), color, boundaryThickness)
#	cv2.rectangle(canvas, (startPointX, startPointY), (startPointX + width, startPointY + height), color, boundaryThickness)
startX = 250
startY = 200
cv2.rectangle(canvas, (startX, startY), (startX + 250, startY +150), color = (0,255,0), thickness = -1)# -1 fills the rectangle. 
cv2.rectangle(canvas, (startX, startY), (startX + 50, startY + 150), color = (255,0,0), thickness = 2)
cv2.rectangle(canvas, (startX, startY), (startX + 100, startY + 100), color = (0,0,255), thickness = 3)
cv2.rectangle(canvas, (startX, startY), (startX + 150, startY + 150), color = (255,0,100), thickness = 5)

cv2.imshow('Drawing',canvas)
cv2.waitKey(0)
