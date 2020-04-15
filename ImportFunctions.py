#	Angkan Biswas
#	15.4.2020
#	Different ways of calling different functions of other modules/libraries.

imgPath = '/home/sangeeta/Python/frog.jpeg'

#------------------------------------------------------
import cv2
import skimage

img = cv2.imread(imgPath)
saltyImg = skimage.util.random_noise(img)
#------------------------------------------------------

#------------------------------------------------------
from cv2 import imread
from skimage.util import random_noise

img = imread(imgPath)
saltyImg = random_noise(img)
#------------------------------------------------------

#------------------------------------------------------
from skimage.util import random_noise as rn
import numpy as np

saltyImg = rn(img)
concateImg = np.concatenate((img,saltyImg), axis = 1)
#------------------------------------------------------

#------------------------------------------------------
from numpy import concatenate as ct

concateImg = ct((img,saltyImg), axis = 1)
#------------------------------------------------------
