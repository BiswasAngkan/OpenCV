#	Angkan Biswas
#	08.05.2019
#	To save a picture taken by the web camera.

import cv2

camera = cv2.VideoCapture(0)						#	Get access of the web camera.
cameraStatus, picture = camera.read()					#	Take a picture using the camera.
imgFileName = '/home/del/Example/GitHub/Picture/MyPicture.jpg'
cv2.imwrite(imgFileName, picture)					#	Save picture
		
camera.release()							#	Release the captured camera
