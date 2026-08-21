import os

import firebase_admin
import numpy as np
import pyrebase
from firebase_admin import credentials, firestore
from PIL import Image
from tflite_runtime.interpreter import Interpreter

from classification.config import (
    FIREBASE_CONFIG, FIREBASE_EMAIL, FIREBASE_PASSWORD,
    FIREBASE_SERVICE_ACCOUNT_PATH, TFLITE_MODEL_PATH,
    IMAGE_PREDICTION_DIR,
)
from classification.iot.camera import upload_image
from classification.iot.capteur import temperatureHumidite
from classification.src.prediction import classify_image


def get_firebase_app():
    """Initialize and return pyrebase Firebase app."""
    return pyrebase.initialize_app(FIREBASE_CONFIG)


def predict_and_push(image_name="Early_blight2.jpg"):
    """Run prediction on an image and push results to Firebase."""
    interpreter = Interpreter(TFLITE_MODEL_PATH)
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']

    image_path = os.path.join(IMAGE_PREDICTION_DIR, image_name)
    img = Image.open(image_path).convert('RGB').resize((width, height))

    temperature, humidite = temperatureHumidite()
    result = str(classify_image(interpreter, img))

    firebase = get_firebase_app()
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(FIREBASE_EMAIL, FIREBASE_PASSWORD)

    data = {
        "temperature": temperature,
        "humidite": humidite,
        "Plant sante": result,
        "image": upload_image(image_name=image_name),
    }

    database = firebase.database()
    database.child("historique").push(data, user['idToken'])


def push_to_firestore(temperature, humidite, image_name, result):
    """Push data to Cloud Firestore."""
    cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    db.collection('historique').add({
        'temperature': str(temperature),
        'humidite': str(humidite),
        'image': image_name,
        'resultatTest': result,
    })


if __name__ == '__main__':
    predict_and_push()
