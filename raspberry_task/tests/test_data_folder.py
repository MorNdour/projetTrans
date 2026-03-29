# Test for data folder existence in src
import os

def test_data_folder_exists():
    assert os.path.exists('../src/data')
