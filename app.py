import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Flower Classification App",
    page_icon="🌸",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("flower_transfer_model.h5")
    return model

model = load_model()

# -------------------------------
# Class Names (same order as training)
# -------------------------------
CLASS_NAMES = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# -------------------------------
# Image Preprocessing
# -------------------------------
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# -------------------------------
# UI
# -------------------------------
st.title("🌸 Flower Classification App")
st.write("Upload an image and the model will predict the flower type.")

uploaded_file = st.file_uploader(
    "Choose a flower image",
    type=["jpg", "jpeg", "png" , "jfif"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)

        predicted_class = CLASS_NAMES[np.argmax(predictions)]
        confidence = np.max(predictions) * 100
        
       
    # ---- CONFIDENCE CHECK ----
        if confidence < 60:
            st.warning("❌ This does not look like a flower.")
        else:
            st.success(f"🌸 Prediction: **{predicted_class}**")
            st.info(f"🔍 Confidence: **{confidence:.2f}%**")
            
    