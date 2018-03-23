import pytest

def f():
    raise SystemExit()

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# running command:pytest -q test_sysexit.py