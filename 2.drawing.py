import cv2
import numpy as np

#Python2/Python3 

canvas = np.zeros((300,300,3), dtype='uint8')
color = (0,255,0)

img_height = canvas.shape[0]
img_width = canvas.shape[1]

'''
Lines:

#1 - upper left corner - lower right corner (green color)
#2 - lower left corner - upper right corner (blue color)

args: <image>, <starting point tuple>, <ending point tuple>, <color tuple>, <t
<thickness in px>


'''
cv2.line(canvas, (0,0), (img_width, img_height), color, 4)
cv2.line(canvas, (0, img_height), (img_width,0), (255,0,0), 4)


'''
Rectangles:
args: <image> ,<upper left point coords>, <lower right point coords>, <color tuple>
<thickness in px> - if thickness value is -1, the rectangle is color filled

'''

cv2.rectangle(canvas, (100,100),(200,200), (0,0,255), 3)
cv2.rectangle(canvas, (150,150),(250,250), (0,255,255), -1)

'''
Circles;

args: <image>, <center coords>, <radius value>, <color tuple>, <thickness>, 
if thickness value is -1, the circle is color filled

'''

cv2.circle(canvas, (img_width//2, img_height//2), 50, (255, 0, 255), 3)
cv2.circle(canvas, (img_width//2, img_height//2), 45, (255, 255, 0), -1)

cv2.imshow("Canvas image", canvas)
cv2.waitKey(0)                  


