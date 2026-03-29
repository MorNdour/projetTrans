# Test for cnn_model_save.h5 existence
import os

def test_cnn_model_save_exists():
    assert os.path.exists('../cnn_model_save.h5')
