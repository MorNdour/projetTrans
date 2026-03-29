# Test for capture folder existence
import os

def test_capture_exists():
    assert os.path.exists('../capture')
