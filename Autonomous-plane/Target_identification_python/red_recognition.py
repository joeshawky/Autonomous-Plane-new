import numpy as np
import cv2
from erkam_geo import *
import pathes
#if our text file is empty then the code will malfunction because we're 
#converting whatever is in test.txt to int. if it is empty it adds
# a 0 to avoid getting an error
def empty_file(file):
    file = open(file, "r+")
    value = file.read()
    if(value == "" or value == "0"):
        file.write("30000000000")
    file.close()



# def boundary(foto):
#     img = cv2.imread(foto)
#     img_height = img.shape[0]
#     img_width = img.shape[1]

#     boundary_left_x = (img_width/2) - 100
#     boundary_right_x = (img_width/2) + 100
#     boundary_left_y = (img_height/2) - 100
#     boundary_right_y = (img_height/2) + 100
#     return boundary_left_x, boundary_right_x, boundary_left_y, boundary_right_y

def find_red(foto):
    index = 1
    img = cv2.imread(foto)
    # boundary_left_x, boundary_right_x, boundary_left_y, boundary_right_y = boundary(foto)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #converts our image from BGR to HSV format
    
    #hsv color ranges for red color  
    # lower_red1 = np.array([0, 110, 147])
    # upper_red1 = np.array([10, 255, 255]) 
    # lower_red2 = np.array([160, 140, 147])  #172, 140, 147
    # upper_red2 = np.array([180, 255, 255])

    #bests one so far
    # lower_red1 = np.array([0, 0, 110])
    # upper_red1 = np.array([10, 255, 255]) 
    # lower_red2 = np.array([160, 0, 110])  #172, 140, 147
    # upper_red2 = np.array([180, 255, 255])
    
    lower_red1 = np.array([0, 80, 110])
    upper_red1 = np.array([7, 255, 255]) 
    lower_red2 = np.array([168, 80, 110])  #172, 140, 147
    upper_red2 = np.array([180, 255, 255])
    
    #creating masks that will help us only show red color items in our image
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)


    mask = mask_red1 | mask_red2    #combines the 2 masks we have created
    
    result_red = cv2.bitwise_and(img, img, mask=mask)   #creates a new image with the masks applied
    contours, b = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  #detects all shapes in our image
    # #commentprint("The Total Number of Contours in the Image = ")
    contours_len = len(contours)
    # #commentprint(contours_len)
    
    #since we have a lot of red colored contours in our image
    # we need to pick the biggest possible contour which is our target
    # the next part is used to find the biggest contour (our target) in our image
    # if(contours):
    if(contours_len != 0):
        i = 0
        a = len(contours[0])
        b = 0
        while i < contours_len:     #determines the index of the biggest contour
            if len(contours[i]) > a:
                a = len(contours[i])
                b = i
            i = i + 1
            
        #draws a line arround our contour
        cv2.drawContours(result_red, contours[b], -1, (255, 255, 255), 2)
        cv2.drawContours(img, contours[b], -1, (0, 0, 0), 4)

        #since our contour contains many coordinates, we take the average of 
        #all the coordinates to find our middle point for our target
        target_coordinates = np.mean(contours[b], axis=0, dtype=np.int32) #(x, y)
        
        #defines our x and y coordinates seperately
        x_coordinate = target_coordinates[0][0]
        y_coordinate = target_coordinates[0][1]
        #commentprint("Target's coordinates : {}".format(target_coordinates[0]))
        # print(target_coordinates)
        # #commentprint(contours)

        #draws a diamond shape in the middle of our target
        cv2.line(img, (x_coordinate-2, y_coordinate), (x_coordinate+2, y_coordinate), (0, 255, 0), 2)
        cv2.line(img, (x_coordinate, y_coordinate-2), (x_coordinate, y_coordinate+2), (0, 255, 0), 2)
        cv2.line(result_red, (x_coordinate-2, y_coordinate), (x_coordinate+2, y_coordinate), (0, 255, 0), 2)
        cv2.line(result_red, (x_coordinate, y_coordinate-2), (x_coordinate, y_coordinate+2), (0, 255, 0), 2)

        #shows our modified images
        # cv2.imshow('result red', cv2.resize(result_red, (600,400)))
        # cv2.imshow('image', cv2.resize(img, (600,400))) 
        # cv2.imshow('mask', cv2.resize(mask, (600, 400))) 

        # cv2.waitKey(0)    #prevents images from closing automatically
        x_dist = int(x_coordinate) - (img.shape[1] / 2)
        y_dist = int(y_coordinate) - (img.shape[0] / 2)
        area = abs(pow(x_dist, 2) + pow(y_dist, 2))
        # file = open("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/test.txt", "x")

        empty_file(pathes.area_txt_path)

        read_file = open(pathes.area_txt_path, "r")
        text = read_file.read()
        read_file.close()
        # #commentprint(type(int(text)))
        if(float(area) < float(text)):
            write_file = open(pathes.area_txt_path, "w")
            x_dist = int(x_coordinate) - (img.shape[1] / 2)
            y_dist = (img.shape[0] / 2) - int(y_coordinate)
            write_file.write(str(area))
            write_file.close()

        print("x shape: {}, y shape: {}".format(img.shape[0], img.shape[1]))
        # x_pixel, y_pixel = div_param(pathes.geo_txt_path)
        return (x_dist, y_dist)
        
        #commentprint("Area is: {}".format(area))
        #commentprint("Contour: {}".format(type(contours)))
        #commentprint("Contour len: {}".format(contours_len))
        
    else:
        print("NO RED TARGETS - FUNCTION.PY")
        return 0, 0

        


# print(find_red("{}5.jpeg".format(pathes.pictures_path)))
# print(find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/capture.png"))
# print(find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/color.png"))
# print(find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/1 (1).jpeg"))
# print(find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/4.jpeg")) 
# print(find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/isa.jpeg")) 
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer7.png")
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer2.png")
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer3.png")
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer4.png")
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer5.png")
# find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer6.png")