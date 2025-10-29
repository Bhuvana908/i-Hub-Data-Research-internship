from ultralytics import YOLO
import ffmpeg
import os

# -----------------------
# 1️⃣ Load Local Video
# -----------------------
os.makedirs("videos", exist_ok=True)
video_path = "videos/input.mp4"  # 📂 Place your local video here (rename if needed)



# -----------------------
# 2️⃣ Extract Frames using FFmpeg
# -----------------------
os.makedirs("frames", exist_ok=True)
ffmpeg.input(video_path).output("frames/frame_%04d.jpg", vf="fps=24").run(overwrite_output=True)


# -----------------------
# 3️⃣ YOLOv8 Detection
# -----------------------

detect_model = YOLO("yolov8n.pt")  # Detection model
detect_model.predict(source="frames", save=True, project="processed", name="detect")
print("✅ Detection complete! Results in /processed/detect")

# -----------------------
# 4️⃣ YOLOv8 Segmentation
# -----------------------

seg_model = YOLO("yolov8n-seg.pt")  # Segmentation model
seg_model.predict(source="frames", save=True, project="processed", name="segment")
print("✅ Segmentation complete! Results in /processed/segment")


# Detection video
ffmpeg.input("processed/detect/frame_%04d.jpg", framerate=24).output(
    "output_detection.mp4", vcodec="libx264", pix_fmt="yuv420p"
).run(overwrite_output=True)

# Segmentation video
ffmpeg.input("processed/segment/frame_%04d.jpg", framerate=24).output(
    "output_segmentation.mp4", vcodec="libx264", pix_fmt="yuv420p"
).run(overwrite_output=True)


