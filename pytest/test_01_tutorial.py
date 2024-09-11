import pytest

def test_one_add_one():
    assert 1 + 1 == 2

def test_one_add_two():
    num_1 = 1
    num_2 = 2
    result = 3
    assert num_1 + num_2 == result

def test_divide_by_zero():
    with pytest.raises(Exception) as e:
        res = 5 / 0  

    assert 'division by zero' in str(e.value)
    assert e.type == ZeroDivisionError