from ultralytics import YOLO

#modelo = YOLO('/home/zions/Yolo_test/YOLOV8/Digitos/runs/detect/train9/weights/best.pt')
modelo = YOLO('yolov8n.pt')

res = modelo.train(data='real.yaml',cfg='cfg.yaml')
modelo.val(data='real.yaml')    