import os
import pyream.cd


def test_cd():
    cwd = os.getcwd()
    with pyream.cd.cd('pyream'):
        sub = os.getcwd()
        assert os.path.join(cwd, 'pyream') == sub
    assert os.getcwd() == cwd
