# Test for README.md existence
import os

def test_readme_exists():
    assert os.path.exists('../README.md')
