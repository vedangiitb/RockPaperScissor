from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io
import tensorflow as tf
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        try:
            data = request.get_json()
            time = data.get('time')
            temp = data.get('temperature')
            humidity = data.get('humidity')

            print(time,temp,humidity)
            
            return jsonify({"message": "Data received", "time": time, "temperature": temp, "humidity": humidity})
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Generic server error
    else:
        return "Invalid data format", 400  # Bad request error

if __name__ == '__main__':
    app.run()
