"""
Unit and regression test for the molpy package.
"""

# Import package, test suite, and other packages as needed
import molpy
import pytest
import sys

def test_molpy_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molpy" in sys.modules
