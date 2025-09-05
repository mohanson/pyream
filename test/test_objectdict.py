import pyream.objectdict


def test_objectdict():
    obj = pyream.objectdict.ObjectDict()
    obj.int = 1
    obj.str = 'Hello World'
    assert obj.int == 1
    assert obj.str == 'Hello World'
    assert obj['int'] == 1
    assert obj['str'] == 'Hello World'
