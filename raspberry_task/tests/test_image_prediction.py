# Test for image_prediction folder existence
import os

def test_image_prediction_exists():
    assert os.path.exists('../image_prediction')
