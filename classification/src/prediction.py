import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter

from classification.config import CLASS_NAMES


def classify_image(interpreter, image):
    """Run inference and return the predicted class name."""
    interpreter.invoke()

    output_details = interpreter.get_output_details()[0]
    scores = interpreter.get_tensor(output_details['index'])[0]

    index = int(np.argmax(scores))
    return CLASS_NAMES[index]
