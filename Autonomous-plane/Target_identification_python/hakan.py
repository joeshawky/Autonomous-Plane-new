from pymavlink import mavutil
import time

# global master
# master = connect.master
# master = mavutil.mavlink_connection('udpin:localhost:14550')
master = mavutil.mavlink_connection('tcp:192.168.213.101:5762')
# master = mavutil.mavlink_connection('tcp:192.168.89.101:5762')
# master = mavutil.mavlink_connection('tcp:192.168.31.6:5762')
# master = gps.master
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

# gps.loop(5)
def param_set(param, val):
    master.param_set_send(param, val)

def param_read():
    master.mav.param_request_read_send(
        master.target_system, master.target_component, b'PREV_WP_NUM', -1)

    message = master.recv_match(type='PARAM_VALUE', blocking=True)
    # if(message.param_id == "CAPTURE_WP"):
    if(message.param_id == "PREV_WP_NUM"):
        capture_wp = int(message.param_value)
        print(f"capture wp: {capture_wp}")
        time.sleep(0.5)

# def loop():
    
# while True:
#     param_read()
#     time.sleep(0.2)

param_set("DROP_LAT1", 41103)
param_set("DROP_LAT2", 5553)
param_set("DROP_LNG1", 28548)
param_set("DROP_LNG2", 8132)

# master.param_set_send("DROP_LAT1", 41103)