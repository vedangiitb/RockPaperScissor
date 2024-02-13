from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io
import base64
import tensorflow as tf
import io


app = Flask(__name__)

# Load the pre-trained machine learning model
model = tf.keras.models.load_model('image_classification_model.h5')

class_labels = ['paper', 'rock', 'scissor']

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Receive image data from the request
        image_data = request.data

        img = Image.open(io.BytesIO(image_data))

        img = img.resize((128, 128))  # Resize the image to match model input size
        img_array = np.array(img) / 255.0  # Normalize pixel values

        # Make prediction using the model
        predictions = model.predict(np.expand_dims(img_array, axis=0))

        # Get the predicted class label
        predicted_class_index = np.argmax(predictions)
        predicted_class = class_labels[predicted_class_index]

        # Return the predicted class label
        return jsonify({'prediction': predicted_class}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
