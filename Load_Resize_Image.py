#	Angkan Biswas
#	01.04.2020
#	To show a picture

import cv2 

loadImg = cv2.imread('/home/dell/Example/bench.jpg',0)	

#print(loadImg.shape)				# output will be same as instruction line 15

#print(''.format())

#print(''.format(loadImg.shape))

#print('{}'.format(loadImg.shape))		# output will be same as instruction line 9

print('size of loadImg: {}'.format(loadImg.shape))

resizeImg = cv2.resize(loadImg,(200,200))

print('size of loadImg: {} & resizeImg: {}'.format(loadImg.shape, resizeImg.shape))

title = 'picture'

cv2.imshow(title, resizeImg)

cv2.waitKey(0)
