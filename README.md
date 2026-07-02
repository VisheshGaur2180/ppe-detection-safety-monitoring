# 🦺 AI-Based PPE Detection and Industrial Safety Monitoring System

An AI-powered Personal Protective Equipment (PPE) Detection and Industrial Safety Monitoring System that automatically detects workers, identifies PPE violations, logs safety incidents, generates reports, and provides a web-based interface for monitoring industrial safety using **YOLOv8**, **OpenCV**, and **Flask**.

---

# 📌 Overview

Industrial safety is a critical aspect of manufacturing plants, construction sites, warehouses, and other hazardous workplaces. Ensuring that workers wear the required Personal Protective Equipment (PPE) such as helmets and safety vests is essential for preventing workplace accidents.

This project automates PPE compliance monitoring using a custom-trained **YOLOv8** object detection model. The system processes both images and videos to detect workers, identify missing PPE, highlight safety violations, generate reports, maintain violation logs, and provide a user-friendly Flask web application for monitoring industrial safety.

---

# ✨ Features

- ✅ Real-Time PPE Detection
- ✅ Helmet Detection
- ✅ Safety Vest Detection
- ✅ Person Detection
- ✅ PPE Violation Detection
- ✅ Image Processing
- ✅ Video Processing
- ✅ Automatic Violation Logging
- ✅ CSV Report Generation
- ✅ JSON Log Generation
- ✅ Processed Image Saving
- ✅ Processed Video Saving
- ✅ Flask Web Dashboard
- ✅ Modular Project Architecture
- ✅ Configurable Detection Thresholds

---

# 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- NumPy
- Pandas
- Flask
- ReportLab
- Matplotlib
- HTML
- CSS
- JavaScript

---

# 🏗️ System Architecture

![System Architecture](assets/architecture.png)

---

# 🔄 Workflow

![Workflow](assets/workflow.png)

---

# 📸 Application Screenshots

## Home Page

![Home Page](assets/home_page.png)

---

## Upload Page

![Upload Page](assets/upload_page.png)

---

## PPE Detection Result

![Detection Result](assets/detection_result.png)

---

## Generated Report

![Generated Report](assets/report.png)

---

# 🎥 Project Demo

![Demo](assets/demo.gif)

---

# 📂 Project Structure

```text
ppe-detection-safety-monitoring/
│
├── README.md
├── LICENSE
├── requirements.txt
├── run.py
├── config.py
├── .gitignore
│
├── models/
│   └── best.pt
│
├── src/
│
├── website/
│
├── data/
│   ├── images/
│   └── videos/
│
├── outputs/
│   ├── processed_images/
│   ├── processed_videos/
│   ├── reports/
│   └── logs/
│
└── assets/
    ├── architecture.png
    ├── workflow.png
    ├── home_page.png
    ├── upload_page.png
    ├── detection_result.png
    ├── report.png
    └── demo.gif
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ppe-detection-safety-monitoring.git
cd ppe-detection-safety-monitoring
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Image Detection

```bash
python run.py --mode images
```

### Video Detection

```bash
python run.py --mode video
```

### Complete Pipeline

```bash
python run.py --mode full
```

### Launch Flask Website

```bash
python run.py --mode web
```

---

# 📁 Output

The system automatically generates:

- Processed Images
- Processed Videos
- CSV Reports
- JSON Violation Logs
- Detection Results

---

# 📊 Project Highlights

- Detects workers in industrial environments.
- Identifies helmets and safety vests with high accuracy.
- Detects PPE violations in both images and videos.
- Automatically generates violation logs and reports.
- Provides a clean web interface for monitoring results.
- Modular and scalable architecture for future enhancements.

---

# 🚀 Future Enhancements

- Live CCTV Monitoring
- Multi-Camera Support
- Face Recognition Integration
- Worker Attendance Monitoring
- Email Notifications
- SMS Alerts
- Cloud Deployment
- Mobile Application
- Edge AI Deployment using NVIDIA Jetson
- Dashboard Analytics

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Vishesh Gaur

**B.Tech – Artificial Intelligence & Machine Learning**
