import numpy as np
import cv2 as cv
img = cv.imread('task1.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('out.jpg',res)