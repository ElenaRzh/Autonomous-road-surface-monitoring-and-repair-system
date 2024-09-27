import socket
import cv2
from ultralytics import YOLO
import telebot
from telebot import types
import datetime

token='7328227476:AAHrMjsdEng4qJk66nIq8ni0ZafDFKhvMak'
users = [1412502840,1376407183,368271441,5873101414]
model = YOLO('model.pt')
pits = []
photo_pos = [[0,0.4],[1,0.4],[1,0.8],[1,1.2],[1,1.6],[1,2],[0,2],[0,0.4],[0,0]]
min_dist = 0.15

server = socket.socket()
server.bind(('',9090))
server.listen(1)

client, addr = server.accept()
print('Connected drone:', addr)

for i in range(7):
    image = open(f'image{i}.jpg', mode="wb")
    data = client.recv(2048)
    while True:
        if bytes('Mj!092h', encoding = 'UTF-8') in data:
            image.write(data[:-1])
            image.close()
            break
        image.write(data)
        data = client.recv(2048)
print("Image reception complete.")
client.close()

for i in range(7):
    coor = [0,0,0,0]
    results = model(source=f'image{i}.jpg', show=False, verbose=False)
    for box in results[0].boxes.xyxy:
        for v in range(4):
            coor[v] = int(box[v])
        pits.append([((coor[0]-200)+(coor[2]-200))/2*0.002083+photo_pos[i][0], photo_pos[i][1]-((coor[1]-200)+(coor[3]-200))/2*0.002083])
print(pits)

p1 = 0
while True:
    p2 = 0
    while True:
        if p1 != p2:
            dist = ((pits[p1][0] - pits[p2][0])**2 + (pits[p1][1] - pits[p2][1])**2)**0.5
            if dist < min_dist:
                pits.pop(p2)
        if p2+1 >= len(pits):
            break
        else:
            p2 = p2 + 1
    if p1 + 1 >= len(pits):
        break
    else:
        p1 = p1 + 1

map_img = cv2.imread(r"C:\Users\shers\PycharmProjects\Clover_AI\main_road.jpg")
for pit in pits:
    image = cv2.circle(map_img, (int(pit[0]*500+156), int(1500-(pit[1]*500+190))), 20, (0, 0, 255), -1)
cv2.imwrite(r"C:\Users\shers\PycharmProjects\Clover_AI\road.jpg", map_img)

bot=telebot.TeleBot(token)
for user in users:
    map_img = open('road.jpg', 'rb')
    bot.send_photo(user, map_img, caption=str(datetime.datetime.now()) + f'\nTotal number of pits found:: {len(pits)}')
