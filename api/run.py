import unittest
import threading
import time
import pytest

path = "./"
def get_test_case(path):
    discover = unittest.defaultTestLoader.discover(start_dir=path, pattern="test*")
    return discover

def run(cases):
    run = unittest.TextTestRunner()
    run.run(cases)

if __name__ == '__main__':
    import pytest
    pytest.main(["py.test -d --tx 3*popen"])