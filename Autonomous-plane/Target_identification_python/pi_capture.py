import time
from pymavlink import mavutil

i=0
capture_wp = -1
current_wp = -1

master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
while capture_wp == -1:
    # print("1")
    # master.mav.param_request_read_send(
    #     master.target_system, master.target_component, b'CAPTURE_WP', -15)
    # master.mav.param_request_list_send(
    # master.target_system, master.target_component)

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,    
        0,
        20, 15, -1, 0, 0, 0, 0)

    # message = master.recv_match(type='PARAM_VALUE', blocking=True)
    message = master.recv_match()
    # message = master.recv_match()
    print(message)
    # print("3")
    if(message.param_id == "CAPTURE_WP"):
        capture_wp = int(message.param_value)
        print(f"capture wp: {capture_wp}")
    time.sleep(0.5)

while True:
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0,33, 0, 0, 0, 0, 0, 0)
    
    msg = master.recv_match(type="STATUSTEXT", blocking=True, timeout=0.03)
    if msg != None:
        msg_txt = msg.to_dict()['text']
        if "Reached" in msg_txt:
            current_wp = int( msg_txt.split("#")[1].split(" ")[0])
            print(f"current wp: {current_wp}")

            if current_wp == capture_wp:
                t1=time.time()
                for i in range(0,10):
                    
                    master.mav.command_long_send(
                        master.target_system,
                        master.target_component,
                        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0,33, 0, 0, 0, 0, 0, 0)
                    
                    msg = master.recv_match(type="STATUSTEXT", blocking=True, timeout=0.03)
                    if msg != None:
                        msg_txt = msg.to_dict()['text']
                        if "Reached" in msg_txt:
                            current_wp = int( msg_txt.split("#")[1].split(" ")[0])
                            print(f"current wp: {current_wp}")
                t2=time.time()
                print((t2-t1)/10)
                # with picamera.PiCamera(sensor_mode=2) as cam:
                #     cam.resolution = (1200,900)
                #     cam.framerate = 5
                #     time.sleep(1)
                #     t1=time.time()
                #     try:
                #         (long, lat, alt, hdg)=gps.gps()
                #         (pitch, roll)=gps.pitch_roll()
                #         cam.exif_tags['EXIF.UserComment']= f'{long},{lat},{alt},{hdg},{pitch},{roll}'
                #         cam.capture(f'images/{i}.jpeg', format= 'jpeg', use_video_port=True)
                #     except:
                #         i=i-1
