import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required = True, help = 'Path to the image')

args = vars(ap.parse_args())




image = cv2.imread(args['image'])
cv2.imshow("Image", image)
cv2.waitKey(0)


#rules in OpenCV add and subtract saturate values
# 250 + 10 -> 255
# 220 - 230 -> 0
# all values must be in range [0,255]

#all elements are 100 in matrix
M = np.ones(image.shape, dtype="uint8") * 100


#lighter image
addition_image = cv2.add(image, M)
cv2.imshow("Image 2", addition_image)
cv2.waitKey(0)

#darker image
subtraction_image = cv2.subtract(image, M)
cv2.imshow("Image 3", subtraction_image)
cv2.waitKey(0)


#numpy addition/subtraction
#rules in numpy
#250 + 10 -> 260 % 256 = 4
#220 - 230 -> (-10 + 256) % 256 = 246
#4 - 4 -> (0 + 256) % 256 = 0

added_np = np.add(image,M)
cv2.imshow("np addition", added_np)
cv2.waitKey(0)


sub_np = np.subtract(image,M)
cv2.imshow("np subtraction", sub_np)
cv2.waitKey(0)


subtracted_np = np.subtract(image,M)
cv2.imshow("np subtraction", subtracted_np)
cv2.waitKey(0)








