from function import *
from erkam_geo import *
from dosya import *
from metadata import *
from pymavlink import mavutil
import pathes

count = pic_count(pathes.pictures_path)
# count, lat1, lat2, lon1, lon2 = 0, 0, 0, 0, 0
img_arr = img_array(pathes.pictures_path)
for pic in img_arr:
    if(count != 0):
        print("Pic: {}".format(pic))
        x_pixel, y_pixel = find_red("{}{}".format(pathes.pictures_path, pic))
        if (x_pixel != 0 and y_pixel != 0):
            long, lat, alt, hdg, pitch, roll = metadata("{}{}".format(pathes.pictures_path, pic))
            lat1, lat2, lon1, lon2 = geovdeneme(float(lat), float(long), float(alt), float(hdg), x_pixel, y_pixel, 0, float(pitch), float(roll))
            print(lat1, lat2, lon1, lon2)
    
# pic = "0.jpeg"
# x_pixel, y_pixel = find_red("{}{}".format(pathes.pictures_path, pic))
# long, lat, alt, hdg, pitch, roll = metadata("{}{}".format(pathes.pictures_path, pic))
# lat1, lat2, lon1, lon2 = geovdeneme(float(lat), float(long), float(alt), float(hdg), x_pixel, y_pixel, 0, float(pitch), float(roll))
# print("X: {}, Y: {}".format(x_pixel, y_pixel))
# print(lat1, lat2, lon1, lon2)


master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

if(lat1 != 0 and lat2 != 0 and lon1 != 0 and lon2 != 0):

    # master = mavutil.mavlink_connection('tcp:192.168.213.101:5762')
    master.param_set_send("drop_lat1", lat1)
    master.param_set_send("drop_lat2", lat2)
    master.param_set_send("drop_lon1", lon1)
    master.param_set_send("drop_lon2", lon2)
else:
    master.param_set_send("drop_lat1", 0)
    master.param_set_send("drop_lat2", 0)
    master.param_set_send("drop_lon1", 0)
    master.param_set_send("drop_lon2", 0)


# def processing(i):
    
#     x_pixel, y_pixel = find_red("{}{}.jpeg".format(pathes.pictures_path, str(i)))
#     long, lat, alt, hdg, pitch, roll = metadata("{}{}.jpeg".format(pathes.pictures_path, i))
#     lat1, lat2, lon1, lon2 = geovdeneme(float(lat), float(long), float(alt), float(hdg), x_pixel, y_pixel, 0, float(pitch), float(roll))
#     master.param_set_send("drop_lat1", lat1)
#     master.param_set_send("drop_lat2", lat2)
#     master.param_set_send("drop_lon1", lon1)
#     master.param_set_send("drop_lon2", lon2)
