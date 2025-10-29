# 🎥 Video-Detection-and-Segmentation-YOLOv8

This project demonstrates **object detection** and **segmentation** on videos using **Ultralytics YOLOv8** models.  
It processes an input video (e.g., `input.mp4`), extracts frames, performs detection and segmentation, and then reconstructs the final output videos.

---

## 📊 Project Overview

The project highlights:

- **Object Detection:** Using `yolov8n.pt`  
- **Object Segmentation:** Using `yolov8n-seg.pt`  
- **Frame Extraction & Reconstruction:** Using `FFmpeg`  
- **Automatic Output Saving:** Organized folder structure  

### 🔑 Key Features

- Detect and segment objects in any video  
- Automatically extract frames and recreate output video  
- Outputs stored neatly in folders  
- Easy one-script execution  

---

## 🛠 Tools Used

- **Python ≥ 3.8** → Programming language  
- **Ultralytics YOLOv8** → Pre-trained detection and segmentation models  
- **FFmpeg** → Frame extraction and video creation  
- **ffmpeg-python** → Python interface for FFmpeg  

---

## 📂 Project Files

- **main.py** → Main Python script to run detection and segmentation   
- **frames/** → Extracted video frames  
- **processed/detect/** → Detection output frames  
- **processed/segment/** → Segmentation output frames   
- **requirements.txt** → List of dependencies  
- **README.md** → Project documentation  

---

## 🚀 How to Use

Open a terminal and run the following **bash commands**:

```bash
# Clone the repository
https://github.com/Bhuvana908/i-Hub-Data-Research-internship/tree/main/Video-detection-and-segmentation

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py
```
---

## 📸 Results Preview

## Original Video

[Watch on Google Drive](https://drive.google.com/file/d/1JWzF5-K3AXb0oGHq1xa-Mz2KaKf19XDC/view?usp=sharing)

## Detected Video
[Watch on Google Drive](https://drive.google.com/file/d/1ZbbpyLVQiJouTTjqAuDqsut-u7mb4O0K/view?usp=sharing)

## Segmented Video
[Watch on Google Drive](https://drive.google.com/file/d/19RAxYOrbdAoBzKwms-IISGTptPhlmAah/view?usp=sharing)

---

## 🧠 Learnings from the Project

- **Using YOLOv8 for both object detection and segmentation**  
- **Integrating FFmpeg for video frame processing** 
- **Automating an entire end-to-end video analysis pipeline**  
- **Organizing outputs systematically for reproducibility**


