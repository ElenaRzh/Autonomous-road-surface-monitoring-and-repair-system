from ultralytics import YOLO
model = YOLO('model.pt')
results = model('image.jpg', show=True)
for result in results:
    result.show()