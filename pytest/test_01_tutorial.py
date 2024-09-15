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

test_data = [
    (2, 3, 6),
    (99, 1, 99),
    (0, 10, 0),
    (-5, 1, -5),
    (-5, -2, 10)
]

@pytest.mark.parametrize('num1, num2, result', test_data)
def test_multipication(num1, num2, result):
    assert num1 * num2 == result
