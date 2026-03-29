import pyrebase
from capteur import temperatureHumidite
from camera import image
from tflite_runtime.interpreter import Interpreter
from PIL import Image
import numpy as np
import time
from raspberry_task.src.prediction import classify_image

model_path = "tf_lite_model.tflite"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")
img = "Early_blight2.jpg"

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")

# Load an image to be classified.
images = Image.open("image_prediction/"+img).convert('RGB').resize((width, height))

temperature, humidite = temperatureHumidite()
result = str(classify_image(interpreter,images))
#photo = str(image())

config = {
  "apiKey": "AIzaSyClk5qV1WYYAu2NwGHny9xVDJ4hlyoXUC8",
  "authDomain": "trans-52d35.firebaseapp.com",
  "databaseURL": "https://trans-52d35-default-rtdb.firebaseio.com",
  "projectId": "trans-52d35",
  "storageBucket": "trans-52d35.appspot.com",
  "messagingSenderId": "180416311427",
  "appId": "1:180416311427:web:67a4bdcafbaa59772aabb6",
  "measurementId": "G-PCKTFD33MB"
};

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()

email= "ndourmor2@gmail.com"
password= "trans@sml"
auth = firebase.auth()
user= auth.sign_in_with_email_and_password(email,password)

data={
    "temperature":temperature,
    "humidite": humidite,
    "Plant sante": result,
    "image": image(imageName=img)
}

try:
   database.child("historique").push(data,user['idToken'])
except:
   print("echec d'enregistrement")

import firebase_admin
from firebase_admin import credentials,firestore
import datetime

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#firebase = firebase.FirebaseApplication('', None)


def create():
    today = datetime.datetime.now()
    db.collection('historique').add(
      {
        'temperature': '30',
        'humidite':'45%',
        'image': 'index.png',
        'resultatTest':'health'
      }
    )

create()
