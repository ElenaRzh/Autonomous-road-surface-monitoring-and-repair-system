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
photo_pos = [[0,0.4], [1,0.4], [1,0.8], [1,1.2],[1,1.6], [1,2],[0,2], [0,0.4]]

def go_to(x=0, y=0, z=0.7, yaw=0, speed=0.3, frame_id='aruco_map', auto_arm=False, tolerance=0.15):
    global photo_id
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            rospy.sleep(1)
            frame = rospy.wait_for_message('/main_camera/image_raw', Image)
            img = CvBridge().imgmsg_to_cv2(frame, 'bgr8')
            cv2.imwrite(f'data_img2_{photo_id}.jpg', img)
            photo_id = photo_id + 1
            rospy.sleep(1)
            break

go_to(speed = 1, frame_id='body', auto_arm=True)
go_to(0,0.4)
for pos in photo_pos:
    go_to(pos[0],pos[1])
go_to(0,0,0.6)
land()
