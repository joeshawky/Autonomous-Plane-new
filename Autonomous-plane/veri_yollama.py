from numpy import diff
from pymavlink import mavutil
import time
import math


master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

# master.mav.command_long_send(
#             master.target_system,
#             master.target_component,
#             179, 0, 0, 0, 0, 0, -35.361680, 149.165050, 600)
# master.mav.command_long_send(
#             master.target_system,
#             master.target_component,
#             0,
#             3,
#             mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 
#             0, 0, 0, 0, 0, 0, -35.361680, 149.165050, 600)

mavutil.mavlink.MAVLink_mission_item_message(
            master.target_system,
            master.target_component,
            0,
            3,  
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 
            0, 0, 0, 0, 0, 0, -35.362679, 149.159645, 200)
