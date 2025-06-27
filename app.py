from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Load the trained rice classifier model
model = tf.keras.models.load_model("rice_classification_mobilenet.h5")

class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

# Initialize the Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# Route: Upload Image Page
@app.route("/details")
def details():
    return render_template("details.html")

# Route: Handle Image Upload and Prediction
@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    os.makedirs("static", exist_ok=True)


    image_path = os.path.join("static", "uploaded_image.jpg")
    file.save(image_path)

    # Preprocess
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224)) 
    img_array = np.array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0) 

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    # Render result
    return render_template("results.html", prediction=predicted_class, image_url=image_path)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
