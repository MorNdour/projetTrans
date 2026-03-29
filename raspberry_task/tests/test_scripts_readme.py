# Test for scripts/README.md existence
import os

def test_scripts_readme_exists():
    assert os.path.exists('../scripts/README.md')
