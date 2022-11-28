import enum
import math
from function import *


class Camera():
    def __init__(self, xAngle, yAngle, xPixel, yPixel):
        self.xAngle = xAngle
        self.yAngle = yAngle
        self.xPixel = xPixel
        self.yPixel = yPixel


def addDistance(xdiff, ydiff, xmeterperpixel, ymeterperpixel):
    earthR = 6378137        #6378137
    global lat
    global lon
    global new_latitude
    global new_longitude
    xDistance = xdiff * xmeterperpixel
    yDistance = ydiff * ymeterperpixel
    print("x distance")
    print(round(xDistance, 3))
    print("y distance")
    print(round(yDistance, 3))
    new_latitude  = lat  + (yDistance / (earthR)) * (180 / math.pi)
    # coef = yDistance *  0.0000089
    # new_latitude  = lat  +  coef
    new_longitude = lon + (xDistance / (earthR)) * (180 / math.pi) / math.cos(math.radians(lat))
    return 0

#a = math.tan(30)
def calculateMeterPerPixel(altitude, Camera):
    return  (2 * math.tan(math.radians(Camera.xAngle / 2)) * altitude / Camera.xPixel, 2 * math.tan(math.radians(Camera.yAngle/2)) * altitude / Camera.yPixel)

def calculatePixelDiff(heading, x, y, Camera):
    xDiff1 = -(Camera.xPixel / 2) + x
    yDiff1 = (Camera.yPixel / 2) - y

    xDiff = xDiff1 * math.cos(math.radians(heading)) + yDiff1 * math.sin(math.radians(heading))
    yDiff = xDiff1 * math.sin(math.radians(heading)) + yDiff1 * math.cos(math.radians(heading))
    return (xDiff, yDiff)

img = "C:/Users/PC/Desktop/Vsc/lagari/Target_identification_python/gri.jpg"
#x, y = find_red(img)
x = 3000 #mid = 768
y = 2410  #mid = 10241
#x = 1050 - y = 530
# 71.9 - 72.35
# 52 - 51.98
cam = Camera(72.35, 51.98, 6000, 4000)
# cam = Camera(81, 81, 1126, 2000)
lat = 10
lon = 10
heading = 0
alt = 100
xMeterPerPixel, yMeterPerPixel = calculateMeterPerPixel(alt, cam)
xDiff, yDiff = calculatePixelDiff(heading, x, y, cam)

addDistance(xDiff, yDiff, xMeterPerPixel, yMeterPerPixel)
print("heading:\t\t", heading)
# print(lat,lon)
print(new_latitude, new_longitude)
