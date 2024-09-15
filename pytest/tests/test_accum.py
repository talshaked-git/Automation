from source.accum import Accumulator
import pytest

def test_new_accum():
    accum = Accumulator()
    print(f"default initialization: {accum.count}")
    assert accum.count == 0
    

def test_init():
    accum = Accumulator()
    accum.count = 2
    print(f"manual initialization: {accum.count}")
    assert accum.count == 2

def test_add():
    accum = Accumulator()
    accum.add_count(5)
    print(f"add 5 to count: {accum.count}")
    assert accum.count == 5

def test_add_default():
    accum = Accumulator()
    accum.add_count()
    print(f"add default (1) to count: {accum.count}")
    assert accum.count == 1

def test_get_brand():
    accum = Accumulator
    with pytest.raises(AttributeError) as err:
        print(accum.__brand)
    assert str(err.value) == "type object 'Accumulator' has no attribute '__brand'"
