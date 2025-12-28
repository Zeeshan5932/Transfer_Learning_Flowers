# 🌸 Flower Classification using Transfer Learning + Streamlit

An **end-to-end Deep Learning project** that demonstrates how to train a **Transfer Learning model** and deploy it as an **interactive Streamlit web application**.

This project focuses on **real-world workflow**, not just model training.

---

## 🚀 Project Overview

* **Task:** Multi-class Image Classification
* **Classes:** Daisy, Dandelion, Rose, Sunflower, Tulip
* **Approach:** Transfer Learning with MobileNetV2
* **Deployment:** Streamlit Web App
* **Dataset:** Kaggle Flowers Recognition Dataset

---

## 🧠 Key Concepts Covered

* Transfer Learning (ImageNet pre-trained model)
* Freezing & Fine-tuning CNN layers
* Multi-class classification
* Model serialization (`.h5`)
* ML model → Web App pipeline
* Streamlit-based UI

---

## 🗂 Project Structure

```
flower_classification_project/
│
├── training/
│   └── transfer_learning_training.ipynb
│
├── streamlit_app/
│   ├── app.py
│   ├── flower_classifier.h5
│   └── requirements.txt
│
└── README.md
```

---

## 📊 Model Training

* Trained using **Google Colab (GPU)**
* Used **MobileNetV2** pre-trained on ImageNet
* Custom classification head added
* Fine-tuning applied for better performance

### 🔗 Training Notebook

👉 **[Add Google Colab / Notebook Link Here]**

---

## 🌐 Streamlit Web Application

### Features:

* Upload flower image (jpg / png)
* Real-time prediction
* Confidence score display
* Clean & simple UI

### 🔗 Streamlit App Code

👉 **[[Ai flower classifiers](https://flowersdetection.streamlit.app/)]**

---

## 🛠 Technologies Used

* Python
* TensorFlow / Keras
* MobileNetV2
* NumPy
* PIL
* Streamlit
* Google Colab
* Kaggle

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/streamlit_app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📌 Dataset

* **Flowers Recognition Dataset**
* Source: Kaggle
  👉 [https://www.kaggle.com/datasets/alxmamaev/flowers-recognition](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)

---

## 📈 Future Improvements

* Add Grad-CAM visualization
* Improve UI with charts
* Add model confidence threshold
* Convert backend to FastAPI
* Dockerize the application

---

## 🙌 Feedback & Suggestions

This project is part of my **learning journey**.
I would really appreciate **honest feedback** and suggestions to improve both:

* Model performance
* Code structure
* UI/UX

Feel free to open an issue or connect with me on LinkedIn.

---

## 👤 Author

**Zeeshan Younas**
BS Data Science
Learning ML, DL & AI by building real-world projects

🔗 LinkedIn: *[[Linkedin](https://www.linkedin.com/in/zeeshan-younas-919a09253/)]*

---

## ⭐ If You Like This Project

Give it a ⭐ and share feedback — it helps a lot!

