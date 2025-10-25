import os
from ultralytics import YOLO

# -----------------------------
# 0️⃣ Paths & models
# -----------------------------
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(PROJECT_DIR, "dataset", "vehicle dataset")
data_yaml = os.path.join(PROJECT_DIR, "data.yaml")

# Load pretrained models
model_det = YOLO("yolov8n.pt")       # Pretrained detection model
model_seg = YOLO("yolov8n-seg.pt")   # Pretrained segmentation model

# -----------------------------
# 1️⃣ Collect validation images
# -----------------------------
image_folder = os.path.join(dataset_path, "valid/images")
image_list = [os.path.join(image_folder, f) for f in os.listdir(image_folder)
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# -----------------------------
# 2️⃣ Predict multiple images using pretrained models
# -----------------------------
print("\n=== Running detection predictions (pretrained) ===\n")
for img_path in image_list:
    print(f"Detecting objects in {img_path}...")
    model_det.predict(source=img_path, save=True, project=".", name="runs/detect")

print("\n=== Running segmentation predictions (pretrained) ===\n")
for img_path in image_list:
    print(f"Segmenting objects in {img_path}...")
    model_seg.predict(source=img_path, save=True, project=".", name="runs/segment")

# -----------------------------
# 3️⃣ Train YOLOv8 Detection finally
# -----------------------------
print("\n=== Starting YOLOv8 Detection Training ===\n")
train_model = YOLO("yolov8n.pt")  # Start from pretrained detection model
train_model.train(
    data=data_yaml,   # dataset configuration file
    epochs=3,        # adjust as needed
    imgsz=640,
    batch=8,
    project="runs",
    name="detect_train",
    exist_ok=True
)

# -----------------------------
# 4️⃣ Metrics after training
# -----------------------------
metrics = train_model.val()
print("\nTraining complete! Detection metrics:\n", metrics)

print("\n✅ Workflow complete!")
print("Detection predictions saved in: runs/detect/")
print("Segmentation predictions saved in: runs/segment/")
print("Detection training outputs saved in: runs/detect_train/")
