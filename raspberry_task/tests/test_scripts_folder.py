# Test for scripts folder existence
import os

def test_scripts_folder_exists():
    assert os.path.exists('../scripts')
