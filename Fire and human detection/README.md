# 🔥 YOLOv8 Fire–Human Detection System

This project demonstrates **multi-image and video-based object detection** using YOLOv8, focused on **fire and human detection**, along with evaluation of key performance metrics on a validation set.

---

# 📊 Project Overview

The project highlights:

- **Fire Detection:** Bounding boxes around visible flames 
- **Human Detection:** Identifying humans near fire scenes  
- **Performance Metrics:** Precision, Recall, F1-Score, mAP, Confusion Matrix  

# Key Insights

- Detection results on images and videos containing fire incidents
- Class-wise performance evaluation for fire and humans
- Training and validation results visualized through graphs
- Metrics to analyze real-world fire detection reliability

---

# 🛠 Tools Used

- Python
- Ultralytics YOLOv8
- OpenCV
- NumPy
- PyTorch

---

# 📂 Project Files

- **yolo_detect.py** → Script for image/video inference
- **my_model.pt** → Trained YOLOv8 model
- **Results** → Training outputs:
  - Confusion matrix
  - Precision–Recall curves
  - Loss graphs
  - mAP plots
- **Outputs** → Detected images and videos
- **README.md** → Project documentation

---

# 📦 Dataset

The dataset is **not included in this repository** due to GitHub file size limitations.

**👉 Download the dataset here:**

🔗 https://drive.google.com/file/d/1MKz0vnE9D02ccElSRMXhZWsiKYIwyEAC/view?usp=sharing

**Dataset Details**

- Format: **YOLO**
- Classes:
  - 0 → Fire
  - 1 → Human
 
---

# 📸 Sample Outputs

![Detection](Outputs/output.mp4)

![Detection](Outputs/output1.mp4)

# 📊 Evaluation Metrics & Graph Analysis

After training the YOLOv8 model, multiple evaluation metrics and graphs were generated to assess detection performance.

**🔹 F1–Confidence Curve**

![F1](Results/BoxF1_curve.png)


**🔹 Precision–Confidence Curve**

![Precision](Results/BoxP_curve.png)


**🔹 Precision–Recall Curve**

![PR](Results/BoxPR_curve.png)


**🔹 Recall–Confidence Curve**

![Recall](Results/BoxR_curve.png)


**🔹 Confusion Matrix**

![Confusion](Results/confusion_matrix.png)
![Confusion](Results/confusion_matrix_normalized.png)


**Training & Validation Metrics Overview**

![Results](Results/results.png)

  
---

# 🔍 Explanation for Lower Fire Detection Accuracy

The fire class shows comparatively lower accuracy than human detection due to real-world visual challenges and dataset limitations, which are common in fire detection tasks.

## 🔥 Key Reasons

- **No fixed shape:** Fire is a highly dynamic object with irregular boundaries that change frame-to-frame, making it harder for YOLO to learn stable spatial     features.
- **Visual similarity with background:** Fire often overlaps with bright backgrounds such as sunlight, lamps, reflections, or warm-colored objects, causing confusion    between fire and background.
- **Small or distant fire regions:** Flames often occupy small pixel areas, which are difficult for object detectors to localize accurately.
- **Lighting and smoke variations:** Fire appearance varies significantly across indoor/outdoor, day/night, and smoke-covered scenes.

From the **confusion matrix**, it is evident that many fire instances are misclassified as background, indicating low contrast and ambiguous visual features rather than model failure.

---

# 🔑 Learnings & Takeaways

- Building a **custom YOLOv8 dataset for fire detection**
- Training YOLOv8 for **human safety and fire monitoring**
- Evaluating detection models using **mAP, Precision, Recall, and F1-score**
- Handling challenging fire backgrounds and occlusions

# 👤 Author

**Kadasani Bhuvana Reddy** </br>
Computer Science Engineering (CSE) </br>
Fire–Human Detection System using YOLOv8
