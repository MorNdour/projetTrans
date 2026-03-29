# Test for tf_lite_model.tflite existence
import os

def test_tf_lite_model_exists():
    assert os.path.exists('../tf_lite_model.tflite')
