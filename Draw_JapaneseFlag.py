# Angkan Bsiwas
# 06.05.2020
# To draw the Japanese Flag using OpenCV's functions.

import cv2
import numpy as np

w = int(input('width: '))
h = int(input('height: '))

canvas = np.zeros((h, w, 3))

rX = int(w/4); rY = int(h/4)
S1X = int(w/2); S1Y = 0; E1X = int(w/2); E1Y = h; S2X = 0 ; S2Y = int(h/2); E2X = w; E2Y = int(h/2)
cX = int(w/2) ; cY = int(h/2); cR = int(h/5)

cv2.rectangle(canvas, (rX, rY), (3*rX, 3*rY), color = (10,10,10), thickness = -1)  	# -1 fills the rectangle. 
cv2.line(canvas, (S1X, S1Y), (E1X, E1Y), color = (255,0,0), thickness = 1)
cv2.line(canvas, (S2X, S2Y), (E2X, E2Y), color = (0,255,0), thickness = 1)
cv2.circle(canvas, (cX, cY), cR, color = (0,0,255), thickness = -1)

cv2.imshow('Drawing',canvas)
cv2.waitKey(0)  
