# MLAnnotator

MLAnnotator is an automated annotation tool for object detection models using CoreML.

## 📌 Features
- Automatically assigns labels based on image filenames.
- Generates `annotations.json` in a Create ML-compatible format.
- Uses full-image bounding boxes for easy training.
- Works with Create ML for training object detection models.

## 📂 Project Structure
```
📂 MLAnnotator
├── 📂 dataset           # Store original images
├── 📂 scripts           # Annotation scripts
│   ├── generate_annotations.py   # Automated annotation tool
├── 📂 models            # Store trained .mlmodel files
├── 📂 annotations       # JSON annotation files
│   ├── annotations.json # Automatically generated annotations
├── 📄 README.md         # Project instructions
├── 📄 requirements.txt  # Dependencies
```

## 🚀 Getting Started
### 1️⃣ Install Dependencies
Ensure Python 3 and the required libraries are installed:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Annotation Tool
```bash
python3 scripts/generate_annotations.py
```
- **Select your image folder** when prompted.
- The tool will **automatically label each image**.
- The bounding box will cover the **entire image**.
- The labeled data will be saved as `annotations.json`.

### 3️⃣ Train the Model in Create ML
1. Open **Create ML** and select **New Object Detection Project**.
2. Choose the dataset folder:
   ```bash
   /Users/jonniakesson/Desktop/CardDataset/
   ```
3. Click **Train** and wait for the process to complete.
4. Export the trained **`.mlmodel`** file.

### 4️⃣ Use the Model in SwiftUI
- Drag the exported `.mlmodel` into your **Xcode** project.
- Integrate it into your SwiftUI app for real-time object detection.

