import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required = True, help = 'Path to the image')

args = vars(ap.parse_args())


def get_image_height_width(image):
    return image.shape[:2]
def translate(image, delta_x = None, delta_y = None, M = None):
    img_height, img_width = get_image_height_width(image)
    if(M is None): M = np.float32([[1,0, delta_x],[0,1,delta_y]])

    return cv2.warpAffine(image, M, (img_width, img_height))


image = cv2.imread(args['image'])
img_height, img_width = image.shape[:2]
cv2.imshow("Image", image)
cv2.waitKey(0)

shifted = translate(image, -20, 50)
cv2.imshow("Translated image", shifted)
cv2.waitKey(0)

(h,w) = get_image_height_width(image)
M2 = cv2.getRotationMatrix2D((w//2,h//2), 90, 2)
rotated = translate(image, M = M2)
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)

