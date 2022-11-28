from pymavlink import mavutil
import time
import math
master = mavutil.mavlink_connection('udpin:localhost:14550')
# master = connect.master
# connect.master = master
# master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
# master = mavutil.mavlink_connection('tcp:192.168.225.253:5762')
# master = mavutil.mavlink_connection('tcp:192.168.213.251:5762')
# master = mavutil.mavlink_connection('tcp:192.168.213.253:5762')
# global master
# master = mavutil.mavlink_connection('tcp:192.168.31.6:5762')
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
print("test")
global times
global successful
successful = 0
times = 0


# def gps_testing():
#     global successful
#     try:
#         master.mav.command_long_send(
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,    
#         0,
#         33, 0, 0, 0, 0, 0, 0)
#         #33
#         konum = master.recv_match(type="GLOBAL_POSITION_INT", blocking=True, timeout=0.03)
                        
#         if konum is not None:
#             gpsdic = konum.to_dict()
                        

#             lat = gpsdic["lat"] / math.pow(10, 7)
#             long = gpsdic["lon"] / math.pow(10, 7)

                        
#             #commentprint("long: " + str(long))
#             #commentprint("lat: " + str(lat))
#             # with open("gps.txt", "a") as f:
#             #         f.write("long: " + str(long) + "\n")
#             #         f.write("lat: " + str(lat) + "\n")
#             # diff = time.time() - times
#             # times = time.time()
#             # #commentprint("Time: " + str(times))
#             # #commentprint("diff: " + str(diff) + "\n")
#             # sys.exit(1)
#             # quit()
#             successful = successful + 1
            
#             # time.sleep(0.4)
#             raise Exception("DONE")
#         else:
#             gps()
#     except Exception as ex:
#         #commentprint(ex)
#         # time.sleep(0.4)
#         pass
#     return NULL

def gps():
    try:
        master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,    
        0,
        33, 1000000, 0, 0, 0, 0, 0)
        konum = master.recv_match(type="GLOBAL_POSITION_INT", blocking=True, timeout=0.03)
        #commentprint("----> {}".format(konum))
        if konum is not None:
            gpsdic = konum.to_dict()
                        
            lat = gpsdic["lat"] / math.pow(10, 7)
            long = gpsdic["lon"] / math.pow(10, 7)
            alt = gpsdic["relative_alt"] / math.pow(10, 3)
            hdg = gpsdic["hdg"] / math.pow(10, 2)
            print("long: " + str(long))
            print("lat: " + str(lat))
            print("alt: " + str(alt))
            print("hdg: " + str(hdg))
            time.sleep(1)
            return long, lat, alt, hdg
        else:
            # print("HEY")
            gps()
    except Exception as ex:
        #commentprint(ex)
        # time.sleep(0.4)
        pass
    return None

def pitch_roll():
    try:
        master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,    
        0,
        30, 0, 0, 0, 0, 0, 0)
        konum = master.recv_match(type="ATTITUDE", blocking=True, timeout=0.03)
        #commentprint("----> {}".format(konum))
        if konum is not None:
            gpsdic = konum.to_dict()
            pitch = gpsdic["pitch"] * 180/math.pi
            roll = gpsdic["roll"] * 180/math.pi
            #commentprint("pitch: " + str(pitch))
            #commentprint("roll: " + str(roll))
            return pitch, roll
        else:
            pitch_roll()
    except Exception as ex:
        #commentprint(ex)
        # time.sleep(0.4)
        pass
    return None

# gps()

def param_set(param, val):
    master.param_set_send(param, val)


def loop(x):
    i = 0
    tm = 0
    global successful
    while i in range(x):
        times = time.time()
        #commentprint("i : {}".format(i))
        # pitch_roll()
        gps()
        diff = time.time() - times
        tm = tm + diff
        # print("Time: " + str(times))
        # print("diff: " + str(diff) + "\n")
        # print()
        i = i + 1
        successful = successful + 1
    avg = tm/successful
    # print("Successfuly done {} times out of {} times".format(successful, i))
    # print("AVERAGE: {}".format(avg))
    return avg

# pitch_roll()
# loop(1000)


def wp():
    try:
        master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,    
        0,
        77, 0, 0, 0, 0, 0, 0)
        konum = master.recv_match(type="COMMAND_ACK", blocking=True, timeout=0.03)
        # konum = master.recv_match(timeout=0.03)
        # konum = master.recv_match(type="HIGH_LATENCY2 ", blocking=True, timeout=0.03)
        print(konum)
        #commentprint("----> {}".format(konum))
        if konum is not None:
            gpsdic = konum.to_dict()
            print(gpsdic)
            # pitch = gpsdic["pitch"] * 180/math.pi
            # roll = gpsdic["roll"] * 180/math.pi
            #commentprint("pitch: " + str(pitch))
            #commentprint("roll: " + str(roll))
            print("za")
        else:
            print("t1")
            wp()
    except Exception as ex:
        #commentprint(ex)
        # time.sleep(0.4)
        pass
    return None


# loop(100)
param_set("drop_lat1", 2310)
# gps()