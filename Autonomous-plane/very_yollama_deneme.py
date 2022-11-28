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

def get_location_metres(original_location, dNorth, dEast):
    """
    Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the 
    specified `original_location`. The returned Location has the same `alt` value
    as `original_location`.

    The function is useful when you want to move the vehicle around specifying locations relative to 
    the current vehicle position.
    The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
    For more information see:
    http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
    """
    earth_radius=6378137.0 #Radius of "spherical" earth
    #Coordinate offsets in radians
    dLat = dNorth/earth_radius
    dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

    #New position in decimal degrees
    newlat = original_location.lat + (dLat * 180/math.pi)
    newlon = original_location.lon + (dLon * 180/math.pi)
    return LocationGlobal(newlat, newlon,original_location.alt)


def get_distance_metres(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two LocationGlobal objects.

    This method is an approximation, and will not be accurate over large distances and close to the 
    earth's poles. It comes from the ArduPilot test code: 
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

def distance_to_current_waypoint():
    """
    Gets distance in metres to the current waypoint. 
    It returns None for the first waypoint (Home location).
    """
    nextwaypoint = vehicle.commands.next
    if nextwaypoint==0:
        return None
    missionitem=vehicle.commands[nextwaypoint-1] #commands are zero indexed
    lat = missionitem.x
    lon = missionitem.y
    alt = missionitem.z
    targetWaypointLocation = LocationGlobalRelative(lat,lon,alt)
    distancetopoint = get_distance_metres(vehicle.location.global_frame, targetWaypointLocation)
    return distancetopoint


cmd1= add_waypoint(-35.3641359, 149.1513777, 150)
cmd2= add_waypoint(-35.3641709, 149.1598749, 150)
cmd3= add_waypoint(-35.3585012, 149.1600466, 150)
cmd4= add_waypoint(-35.3588512, 149.1508627, 150)
 

vehicle.commands.next = 0
vehicle.mode = VehicleMode("AUTO")
i = 4
while True:
    nextwaypoint = vehicle.commands.next
    print('next waypoint: ' + str(nextwaypoint))
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)   

    if(nextwaypoint == i):
        print("t1")
        delete_waypoint()
        print("t2")
        vehicle.mode = VehicleMode("AUTO")
        print("t3")
        cmd_temp = add_waypoint(-35.3588900, 149.1508780, 150)
        i = i + 1

        
    time.sleep(1)
