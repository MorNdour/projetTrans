#from picamera import PiCamera
#from time import sleep
#import os
#import datetime

import pyrebase

from classification.config import FIREBASE_CONFIG, FIREBASE_EMAIL, FIREBASE_PASSWORD


def _get_firebase():
    return pyrebase.initialize_app(FIREBASE_CONFIG)


def upload_image(image_name="index.jpg"):
    """Upload an image to Firebase Storage and return its public URL."""
    firebase = _get_firebase()
    auth = firebase.auth()
    storage = firebase.storage()
    image_url = "aucun url"

    try:
        name = "/home/trans/trans/image_prediction/" + image_name
        user = auth.sign_in_with_email_and_password(FIREBASE_EMAIL, FIREBASE_PASSWORD)
        storage.child("image/" + image_name).put(name, user['idToken'])
        image_url = storage.child("image/" + image_name).get_url(user["idToken"])
    except Exception:
        print("error")

    return image_url


if __name__ == '__main__':
    print(upload_image())
