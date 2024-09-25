
# Подготовка датасета
Для тестирования и отладки мы распечатали карту с имитацией дорожного полотна.

<img src="https://github.com/user-attachments/assets/db438641-c850-4cc7-a689-71e5e0eeebdb" width="400" height="600">


На карте мы разместили фотографии ям разных размеров. Также на некоторые ямы дополнительно были добавлены различные эффекты искожения цвета. После этого мы приступили к подготке датасета.
Датасет для обучения нейронной сети создавался с помощью кода:
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

Этот код выполняет облет улиц делая снимки дорожного полотна. Всего мы выполнили 9 пролетов, изменяя после каждого пролета расположение ям,а также освещение и добавляя различные лишние предметы на поле. Собрав около 300 фотографий, мы загрузили их на сайт [roboflow](
https://app.roboflow.com/login), чтобы обработать и обучить нейронную сеть на распознование ям.

![data_img_10](https://github.com/user-attachments/assets/5ff84f07-7390-4d1f-8c10-0e6caf8e60da)

# Обучение и тесты нейронной сети

Нейронную сеть мы обучали при помощи сервиса Google Сollab. 
После обучения мы получили модель нашей нейронной сети в формате '.pt' и приступили к ее тестам. Для тестов использовали следующий код:
```python
from ultralytics import YOLO
model = YOLO('model.pt')
results = model('image.jpg', show=True)
for result in results:
    result.show()
```
Этот код обрабатывает изображение и выводит результат обработки в окно. 

![ямы обработанные](https://github.com/user-attachments/assets/a4888274-f317-4aed-aef5-890789c613bc)

 # Работа с результатами распознования

 




