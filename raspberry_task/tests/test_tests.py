# Test for tests folder existence
import os

def test_tests_exists():
    assert os.path.exists('../tests')
