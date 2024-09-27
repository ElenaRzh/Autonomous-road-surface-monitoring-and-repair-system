import socket
import time
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from clover import srv
import math
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

photo_id = 0
positions = [[0,0.4], [1,0.4], [1,0.8], [1,1.2], [1,1.6], [1,2], [0,2]]

def go_to(x=0, y=0, z=0.7, yaw=-1.57, speed=0.3, frame_id='aruco_map', auto_arm=False, tolerance=0.03):
    global photo_id
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            frame = rospy.wait_for_message('/main_camera/image_raw', Image)
            img = CvBridge().imgmsg_to_cv2(frame, 'bgr8')
            cv2.imwrite(f'data_img_{photo_id}.jpg', img[40:440, 120:520])
            photo_id = photo_id + 1
            rospy.sleep(1)
            break

navigate(x=0, y=0, z=0.7, speed = 1, frame_id='body', auto_arm=True)
rospy.sleep(2)
for pos in positions:
    go_to(pos[0],pos[1])
go_to(0,0,0.6, tolerance=0.1)
land()

client = socket.socket()
client.connect(('10.0.0.19', 9090))
for n in range(7):
    print(f'data_img_{n}.jpg')
    send_img = open(f'data_img_{n}.jpg', mode="rb")
    data = send_img.read(2048)
    while data:
        client.send(data)
        data = send_img.read(2048)
    client.send(bytes('Mj!092h', encoding = 'UTF-8'))
    send_img.close()
    time.sleep(1)
client.close()