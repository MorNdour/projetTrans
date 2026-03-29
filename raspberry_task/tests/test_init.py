# Test for __init__.py existence in src
import os

def test_init_exists():
    assert os.path.exists('../src/__init__.py')
