# Test for __main__.py existence
import os

def test_main_exists():
    assert os.path.exists('../src/__main__.py')
