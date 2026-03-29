# Test for models folder existence
import os

def test_models_exists():
    assert os.path.exists('../src/models')
