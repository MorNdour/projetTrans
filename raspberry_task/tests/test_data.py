# Test for data folder existence
import os

def test_data_exists():
    assert os.path.exists('../data')
