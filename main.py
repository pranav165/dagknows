#!/usr/bin/env python3
import urllib3
import pytest
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disable ssl warning

if __name__ == '__main__':
    exit_code = pytest.main(sys.argv[1:])
