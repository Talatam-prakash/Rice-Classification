# 🌾 Rice Grain Classification Web App

A deep learning-based web application that classifies different varieties of rice grains from an uploaded image. This project uses **MobileNetV2 (Transfer Learning)** for high accuracy and is integrated into a Flask-based web interface.

---

## 📌 Project Highlights

- 5 Rice Varieties: Arborio, Basmati, Ipsala, Jasmine, Karacadag
- Achieved **98% accuracy** on both training and test sets
- Lightweight, fast, and accurate with **MobileNetV2**
- Built with **TensorFlow**, **Pillow**, **Flask**, and **Bootstrap**
- Fully interactive web UI for real-time predictions

---

## 🏗️ Project Structure

```
rice-grain-classification/
├── app.py                         # Flask web app
├── rice_classification_mobilenet.h5  # Trained MobileNetV2 model
├── requirements.txt              # All dependencies
├── static/
│   ├── style.css                 # Custom CSS styling
│   ├── background.jpg            # Webpage background image
│   └── uploaded_image.jpg        # Uploaded image (dynamic)
├── templates/
│   ├── index.html                # Homepage
│   ├── details.html              # Upload page
│   └── results.html              # Prediction result page
└── README.md
```

---

## ⚙️ How It Works

1. **Model**: MobileNetV2 pretrained on ImageNet, fine-tuned on rice grain dataset
2. **Image Input**: User uploads an image via the web interface
3. **Prediction**: Image is preprocessed and passed to the model
4. **Output**: Predicted rice variety is displayed with the uploaded image

---

## Getting Started

###  Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/rice-classification.git
cd rice-grain-classification

# Create virtual environment (optional but recommended)
python3 -m venv rice
source rice/bin/activate  # or rice\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### Run the Web App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to start using the app.

---

##  Dataset

Rice Image Dataset by [Murat Koklu](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) (via Kaggle) containing 5 rice grain categories with 1500 images each.

---



##  Tech Stack

- TensorFlow / Keras
- Pillow (Image processing)
- Flask (Web framework)
- HTML + CSS + Bootstrap

---


##  License

This project is licensed under the MIT License.

---
