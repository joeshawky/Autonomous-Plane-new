from pymavlink import mavutil
global master

# master = mavutil.mavlink_connection('udpin:localhost:14550')
master = mavutil.mavlink_connection('tcp:192.168.31.6:5762')

master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

import gps