#from picamera import PiCamera
#from time import sleep
#import os
#import datetime

import pyrebase

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

#camera = PiCamera()
def image(imageName="index.jpg",imageUrl="aucun url"):
    auth = firebase.auth()
    #Enter your user account details
    email = "ndourmor2@gmail.com"
    password = "trans@sml"
    try:
       #dt = str(datetime.datetime.now())
       name = "/home/trans/trans/image_prediction/"+imageName
       #camera.capture(name)
       #imageUrl = name
       user = auth.sign_in_with_email_and_password(email, password)
       storage.child("image/"+imageName).put(name,user['idToken'])
       imageUrl = storage.child("image/"+imageName).get_url(user["idToken"])
       #sleep(2)
    except:
        #camera.close()
        print("error")
    return imageUrl

print(image())
