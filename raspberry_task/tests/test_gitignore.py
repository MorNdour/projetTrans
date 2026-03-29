# Test for .gitignore existence
import os

def test_gitignore_exists():
    assert os.path.exists('../.gitignore')
