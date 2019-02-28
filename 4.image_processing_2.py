import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required = True, help = 'Path to the image')

args = vars(ap.parse_args())

#we want to resize an image (scale) to width = 200px


image = cv2.imread(args['image'])
cv2.imshow("Image", image)
cv2.waitKey(0)



(h,w) = image.shape[:2] 
dim = (200, 200 * h//w)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
cv2.imshow("Resized", resized)
cv2.waitKey(0)


flipped_hor = cv2.flip(image, 0)
flipped_ver = cv2.flip(image, 1)
flipped_both = cv2.flip(image, -1)
cv2.imshow("Flipped horizontally", flipped_hor)
cv2.waitKey(0)


cv2.imshow("Flipped vertically", flipped_ver)
cv2.waitKey(0)


cv2.imshow("Flipped both", flipped_both)
cv2.waitKey(0)


cropped = image[100:200,100:200]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)


