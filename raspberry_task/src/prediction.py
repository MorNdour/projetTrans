from tflite_runtime.interpreter import Interpreter
from PIL import Image
import numpy as np
import time

def classify_image(interpreter, image):

  # Call the invoke() method from inside a function to avoid this RuntimeError: reference to internal data in the interpreter in the form of a numpy array or slice.
  interpreter.invoke()

  output_details = interpreter.get_output_details()[0]

  scores = interpreter.get_tensor(output_details['index'])[0]
  print(scores)
  max_score = np.max(np.unique(scores))
  index = np.where(scores == max_score)[0][0]
  class_name = ['Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight','Tomato___Leaf_Mold',
              'Tomato___Septoria_leaf_spot','Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot',
              'Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus','Tomato___healthy']
  print(class_name[index])
  return class_name[index]
