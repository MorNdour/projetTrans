# Test for notebooks folder existence
import os

def test_notebooks_folder_exists():
    assert os.path.exists('../notebooks')
