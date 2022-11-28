from function import *
from erkam_geo import *
from dosya import *
import time
i = 0
while True:
    count = pic_count("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp")

    while(i < count):
        x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer{}.png".format(i))
        geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
        print("I ============ {}".format(i))
        time.sleep(1)
        i = i + 1

# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer5.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer3.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer2.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer1.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer6.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer7.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
# x_pixel, y_pixel = find_red("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/mer4.png")
# geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)