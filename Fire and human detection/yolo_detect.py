import os
import sys
import argparse
import glob
import time

import cv2
import numpy as np
from ultralytics import YOLO

# ---------------- ARGUMENTS ----------------
parser = argparse.ArgumentParser()
parser.add_argument('--model', required=True, help='Path to trained YOLO .pt file')
parser.add_argument('--source', required=True, help='Image / folder / video / usb0')
parser.add_argument('--thresh', default=0.5, type=float, help='Confidence threshold')
parser.add_argument('--record', action='store_true', help='Save output video')
args = parser.parse_args()

# ---------------- LOAD MODEL ----------------
if not os.path.exists(args.model):
    print("❌ Model not found")
    sys.exit()

model = YOLO(args.model)
labels = model.names

# ---------------- SOURCE TYPE ----------------
img_ext = ('.jpg', '.jpeg', '.png', '.bmp')
vid_ext = ('.mp4', '.avi', '.mov', '.mkv')

if os.path.isdir(args.source):
    source_type = "folder"
elif os.path.isfile(args.source):
    ext = os.path.splitext(args.source)[1].lower()
    source_type = "image" if ext in img_ext else "video"
elif "usb" in args.source:
    source_type = "usb"
    cam_id = int(args.source.replace("usb", ""))
else:
    print("❌ Invalid source")
    sys.exit()

# ---------------- LOAD SOURCE ----------------
if source_type == "image":
    images = [args.source]
elif source_type == "folder":
    images = [f for f in glob.glob(args.source + "/*") if f.lower().endswith(img_ext)]
elif source_type in ["video", "usb"]:
    cap = cv2.VideoCapture(args.source if source_type == "video" else cam_id)

# ---------------- DISPLAY SETTINGS ----------------
MAX_WIDTH = 900  # 👈 important fix

cv2.namedWindow("YOLO Detection", cv2.WINDOW_NORMAL)

# ---------------- MAIN LOOP ----------------
img_id = 0
fps_buffer = []

while True:

    start = time.perf_counter()

    # ----- Read frame -----
    if source_type in ["image", "folder"]:
        if img_id >= len(images):
            break
        frame = cv2.imread(images[img_id])
        img_id += 1
    else:
        ret, frame = cap.read()
        if not ret:
            break

    # ----- FIX: Downscale large frames -----
    h, w = frame.shape[:2]
    if w > MAX_WIDTH:
        scale = MAX_WIDTH / w
        frame = cv2.resize(
            frame,
            (int(w * scale), int(h * scale)),
            interpolation=cv2.INTER_AREA
        )

    # ----- Inference -----
    results = model(frame, conf=args.thresh, verbose=False)
    detections = results[0].boxes

    # ----- Draw detections -----
    for box in detections:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        name = labels[cls]

        # Bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Label
        label = f"{name} {int(conf * 100)}%"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.8
        thickness = 2

        (tw, th), _ = cv2.getTextSize(label, font, font_scale, thickness)

        y_text = y1 - 10
        if y_text - th < 0:
            y_text = y1 + th + 10

        # Background
        cv2.rectangle(
            frame,
            (x1 - 2, y_text - th - 6),
            (x1 + tw + 6, y_text + 4),
            (0, 0, 0),
            -1
        )

        # Text outline (black)
        cv2.putText(frame, label, (x1 + 2, y_text),
                    font, font_scale, (0, 0, 0),
                    thickness + 3, cv2.LINE_AA)

        # Text (white)
        cv2.putText(frame, label, (x1 + 2, y_text),
                    font, font_scale, (255, 255, 255),
                    thickness, cv2.LINE_AA)

    # ----- FPS -----
    fps = 1 / (time.perf_counter() - start)
    fps_buffer.append(fps)
    if len(fps_buffer) > 30:
        fps_buffer.pop(0)

    cv2.putText(frame, f"FPS: {np.mean(fps_buffer):.1f}",
                (10, 30), font, 0.8, (0, 255, 255), 2)

    # ----- Show -----
    cv2.imshow("YOLO Detection", frame)

    key = cv2.waitKey(0 if source_type in ["image", "folder"] else 1)
    if key in [27, ord('q')]:
        break

# ---------------- CLEANUP ----------------
if source_type in ["video", "usb"]:
    cap.release()

cv2.destroyAllWindows()
print("✅ Finished")
