
 # Pipeline Leak Detection Model

This repository contains the code, trained model, and documentation for detecting pipeline leaks by identifying **gas** and **water leaks** using deep learning. The model was developed using the **Ultralytics YOLOv8** framework, trained on a dataset sourced from Roboflow.

---

## Project Overview

Pipeline leaks can lead to significant environmental and financial consequences. This project aims to develop a robust object detection model to detect leaks by identifying gas and water emissions. The trained model can be integrated into monitoring systems to prevent major pipeline failures.

### Key Features
- Detects gas and water leaks in pipelines.
- Achieves high precision and recall, making it suitable for real-world applications.
- Built on the YOLOv8 architecture for fast and efficient detection.

---

## Dataset Information

The dataset used to train the model was obtained from [Roboflow](https://universe.roboflow.com/gas-leak/pipeline-leak-prediction) under the **CC BY 4.0 License**.

### Dataset Summary
- **Total Images:** 3,586
  - **Training Set:** 3,453 images
  - **Validation Set:** 49 images
  - **Test Set:** 84 images
- **Classes:** Gas Leak, Water Leak

---

## Model Training

### Training Details
- **Framework:** Ultralytics YOLOv8
- **Epochs:** 20
- **Image Size:** 640 × 640 pixels
- **Batch Size:** Auto-configured by YOLOv8
- **Optimizer:** SGD (default in YOLOv8)

### Hardware
- GPU: 20GB memory
- Training Time: ~1.5 minutes per epoch

### Metrics
| Metric         | Value  |
|----------------|--------|
| Precision (P)  | 81.6%  |
| Recall (R)     | 79.4%  |
| mAP@50         | 88.2%  |
| mAP@50-95      | 71.7%  |

---

## Results

The model shows strong performance, achieving high **precision** and **mAP** values, making it suitable for deployment in real-world applications.

### Sample Detection Output
Images showing the detection of gas and water leaks from pipelines can be found in the repository's `results` directory.

---

## Installation

To use this repository, follow these steps:

### Prerequisites
- Python 3.8 or later
- GPU-enabled system for training
- Libraries: Ultralytics, PyTorch, OpenCV, etc.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pipeline-leak-detection.git
   cd pipeline-leak-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from Roboflow and place it in the `data/` folder.

---

## Usage

### Training the Model
To train the model:
```bash
yolo train model=yolov8n.pt data=pipeline_leak.yaml epochs=20 imgsz=640
```

### Testing the Model
To test the model:
```bash
yolo val model=best.pt data=pipeline_leak.yaml
```

### Inference
To run inference on new images:
```bash
yolo detect model=best.pt source=your_image_or_video.mp4
```

---

## Dataset Citation

```
Pipeline-leak-prediction > 2023-10-15 2:31pm
https://universe.roboflow.com/gas-leak/pipeline-leak-prediction
Provided by a Roboflow user
License: CC BY 4.0
```

---

## Acknowledgments

Special thanks to:
- **Roboflow** for providing the dataset.
- The open-source community for developing Ultralytics YOLO.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
