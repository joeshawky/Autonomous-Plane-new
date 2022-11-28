from PythonApplication1 import *
from function import *
import cv2

img = "C:/Users/PC/Desktop/Target_identification_python/test0.jpeg"
x, y= find_red(img)
print(x, y)
cam = Camera(60, 60, 1920, 1080)
lat = 41.05314
lon = 29.01028
heading = 0
alt = 16

xMeterPerPixel, yMeterPerPixel = calculateMeterPerPixel(alt, cam)
xDiff, yDiff = calculatePixelDiff(heading, x, y, cam)

addDistance(1, yDiff * yMeterPerPixel)
addDistance(3, xDiff * xMeterPerPixel)
print(lat,lon)
