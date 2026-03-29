# Test for notebooks/README.md existence
import os

def test_notebooks_readme_exists():
    assert os.path.exists('../notebooks/README.md')
