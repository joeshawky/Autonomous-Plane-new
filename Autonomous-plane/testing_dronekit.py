from dronekit import connect
from dronekit import Command
from dronekit import VehicleMode
from dronekit import LocationGlobal
from pymavlink import mavutil
import math
import time

global vehicle
global cmds
vehicle = connect('127.0.0.1:14550', wait_ready=True)
cmds = vehicle.commands

def delete_waypoint():
    cmds.download()
    cmds.wait_ready()
    cmds.clear()

def add_waypoint(lon, lat, alt):
    cmd = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 
    0, 0, 0, 0, 0, 0, lon, lat, alt)
    cmds.add(cmd)
    cmds.upload()
    return cmd

# delete_waypoint()
cmds.download()
cmds.wait_ready()


missionlist = []

c1 = add_waypoint(-35.3641359, 149.1513777, 150)
# c2 = add_waypoint(-35.3641750, 149.1513790, 150)
# c3 = add_waypoint(-35.3641250, 149.1513490, 150)

print(c1)
# c1.x = 900
# cmds.upload()
print(c1)
# missionlist.append(c1)
# missionlist.append(c2)
# missionlist.append(c3)


# missionlist[1].x = -34
# missionlist[1].y = 150

# print(missionlist[1])
# print(missionlist)
