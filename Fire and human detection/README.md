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

This curve shows how the F1 score varies with confidence thresholds.
The peak F1 score indicates the optimal confidence level for balanced fire and human detection.

**🔹 Precision–Confidence Curve**

![Precision](Results/BoxP_curve.png)

As confidence increases, false positives decrease.
High precision at higher confidence values shows the model reliably detects real fire incidents and humans.

**🔹 Precision–Recall Curve**

![PR](Results/BoxPR_curve.png)

This curve illustrates the trade-off between precision and recall for each class.
The model achieves strong mAP@0.5, indicating accurate detection of fire and humans.

**🔹 Recall–Confidence Curve**

![Recall](Results/BoxR_curve.png)

High recall at lower confidence levels shows the model detects most fire incidents, even in complex scenes.

**🔹 Confusion Matrix**

![Confusion](Results/confusion_matrix.png)
![Confusion](Results/confusion_matrix_normalized.png)

The confusion matrix highlights class-wise prediction accuracy.
Fire and Human classes show strong diagonal values, with minimal misclassification.

**Training & Validation Metrics Overview**

![Results](Results/results.png)

This plot displays training and validation performance across epochs:
- **Loss Curves**: Consistent decrease indicates stable learning
- **Precision & Recall**: Continuous improvement over epochs
- **mAP@50 & mAP@50–95**: Strong generalization ability 
  
---

# 🔑 Learnings & Takeaways

- Building a **custom YOLOv8 dataset for fire detection**
- Training YOLOv8 for **human safety and fire monitoring**
- Evaluating detection models using **mAP, Precision, Recall, and F1-score**
- Handling challenging fire backgrounds and occlusions

# 👤 Author

**Kadasani Bhuvana Reddy**
Computer Science Engineering (CSE)
Fire–Human Detection System using YOLOv8
