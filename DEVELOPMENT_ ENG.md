# Preparing the dataset
For testing and debugging, we printed out a map with an imitation of the roadway.

<img src="https://github.com/user-attachments/assets/db438641-c850-4cc7-a689-71e5e0eeebdb" width="400" height="600">

We have placed photos of pits of different sizes on the map. Also, various color distortion effects were additionally added to some pits. After that, we started to prepare the dataset. The dataset for training the neural network was created using code:

```python
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
```

This code performs a flyby of the streets by taking pictures of the roadway. In total, we completed 9 flights, changing the location of the pits after each flight, as well as lighting and adding various unnecessary items to the field. After collecting about 300 photos, we uploaded them to the [roboflow](https://app.roboflow.com/login) website to process and train the neural network to recognize pits.

![data_img_10](https://github.com/user-attachments/assets/5ff84f07-7390-4d1f-8c10-0e6caf8e60da)

# Neural network training and tests
We trained the neural network using the Google Collab service. After training, we received a model of our neural network in the '.pt' format and started testing it. The following code was used for the tests:
```python
from ultralytics import YOLO
model = YOLO('model.pt')
results = model('image.jpg', show=True)
for result in results:
    result.show()
```
This code processes the image and displays the result of the processing in a window.

![ямы обработанные](https://github.com/user-attachments/assets/a4888274-f317-4aed-aef5-890789c613bc)

# Working with recognition results
After processing the photos with a neural network, we get the coordinates of the pits in pixels. Using trigonometric formulas, we convert coordinates from pixels to meters. Since one pit may be visible in several photos, duplicates may occur. Therefore, we calculate the distance between each pit in pairs and, if it is too small, then remove one of the pits, since it is a duplicate. As a result, we get a list of the coordinates of the detected pits.

We display the detected pits using the [bot's telegrams](). With the OpenCV library, we overlay pits in the form of red circles on the map. After the flyby, the received card is sent to all users specified in the database.

<img src="https://github.com/user-attachments/assets/52269930-f4c1-43ea-8fbc-8d5f3a9c8714" width="400" height="600">

![qrcod](https://github.com/user-attachments/assets/878efc64-b4ef-4c50-8439-afbb6959bfdc)

[**`Demonstration of flight and display of coordinates on the map`**](https://disk.yandex.ru/i/Z1GQtmxnsRyUFA)