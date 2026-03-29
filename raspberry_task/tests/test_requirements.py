# Test for requirements.txt existence
import os

def test_requirements_exists():
    assert os.path.exists('../requirements.txt')
