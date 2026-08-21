import albumentations as A
import cv2
import numpy as np
import tensorflow as tf




def remove_background(image_path):
    """Removes background from an image using HSV color space 
    to isolate green areas."""
    
    image = cv2.imread(image_path)

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green range
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply mask
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Convert BGR → RGB for plotting
    # original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    return result_rgb

IMAGE_SIZE = 256  # or your desired size

resize_and_rescale = tf.keras.Sequential([
    tf.keras.layers.Resizing(IMAGE_SIZE, IMAGE_SIZE),
    tf.keras.layers.Rescaling(1./255),
])

train_transform = A.Compose([
    A.Resize(256,256),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.Rotate(limit=40, p=0.7),
    A.RandomBrightnessContrast(p=0.5),
    A.GaussianBlur(p=0.2),
    # A.CoarseDropout(max_holes=8, max_height=20, max_width=20, p=0.3)
], seed=137)


