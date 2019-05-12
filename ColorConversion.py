#	Angkan Biswas
#	12.05.2019
#	To save an RGB image after converting into a grayscale image.

import cv2

camera = cv2.VideoCapture(0)						#	Get access of the web camera.
_, picture = camera.read()						#	Take a picture using the camera.
camera.release()							#	Release the captured camera

picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)			#	Convert RGB to Grayscale

imgFileName = '/home/dell/Example/GitHub/Picture/BlacK-WhitEPicture.jpg'
cv2.imwrite(imgFileName, picture)					#	Save picture
