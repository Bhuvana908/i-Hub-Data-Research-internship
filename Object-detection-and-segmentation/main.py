from ultralytics import YOLO


model_det = YOLO("yolov8n.pt")       
model_seg = YOLO("yolov8n-seg.pt")   

results_det = model_det.predict(source="bus.jpg", save=True, project=".", name="runs/detect")

results_seg = model_seg.predict(source="bus.jpg", save=True, project=".", name="runs/segment")


