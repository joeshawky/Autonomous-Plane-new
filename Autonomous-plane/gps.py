from pymavlink import mavutil
import time
import math
from datetime import datetime

master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

while True:   

    try:  
        
        gps = master.recv_match()
        # if(gps.get_type() == 'GLOBAL_POSITION_INT'):
        if(gps.get_type() == 'PARAM_REQUEST_LIST '):
            times = time.time()    
            gpsdic = gps.to_dict()
            lat = list(gpsdic.items())[2][1] / math.pow(10, 7)
            long = list(gpsdic.items())[3][1] / math.pow(10, 7)
            print("za")
            # print("long: ", long)
            # print("lat: ", lat)
            # print("time: ", times)
            # print("\n")

        # print(gps)
        
        # print("\n")
        # deneme = list(gps.items())[0][1]
        # lat = list(gpsdic.items())[2][1]
        # long = list(gpsdic.items())[3][1]
        # print(deneme)
        # if deneme == 'GLOBAL_POSITION_INT':
        #     print(gps)
        #     print(long)
        #     print(lat)
    except:
        pass
    time.sleep(0.01)
    # time.sleep(3)
    


# while True:   
 
        
#     gps = master.recv_match()
#     if(gps.get_type() == 'GLOBAL_POSITION_INT'):

#         gpsdic = gps.to_dict()
#         lat = list(gpsdic.items())[2][1] / math.pow(10, 7)
#         long = list(gpsdic.items())[3][1] / math.pow(10, 7)

#         print("long: ", long)
#         print("lat: ", lat)
#         print("\n")

#         # print(gps)
#         # print("\n")
#         # deneme = list(gps.items())[0][1]
#         # lat = list(gpsdic.items())[2][1]
#         # long = list(gpsdic.items())[3][1]
#         # print(deneme)
#         # if deneme == 'GLOBAL_POSITION_INT':
#         #     print(gps)
#         #     print(long)
#         #     print(lat)
    
#     time.sleep(0.000001)