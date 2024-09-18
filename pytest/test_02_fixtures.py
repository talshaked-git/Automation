from source.accum import Accumulator
import pytest

# @pytest.fixture # default scope is 'function'
# def accum():
#     return Accumulator()


# The interperter will look locally for the fixture and use it if it exists, if not, it will look up conftest.py and use the global fixture that fits.
def test_new_accum(accum_global):
    assert accum_global.count == 0
    
@pytest.mark.nightly
def test_init(accum_global):
    accum_global.count = 2
    assert accum_global.count == 2

@pytest.mark.sanity
def test_add(accum_global):
    accum_global.add_count(5)
    assert accum_global.count == 5

@pytest.mark.regression
def test_add_default(accum_global):
    accum_global.add_count()
    assert accum_global.count == 1

def test_get_brand(accum_global):
    with pytest.raises(AttributeError) as err:
        print(accum_global.__brand)
    assert str(err.value) == "'Accumulator' object has no attribute '__brand'"


# pytest .\pytest\test_02_fixtures.py -v -s
# pytest .\pytest\test_02_fixtures.py::test_get_brand -v
# pytest .\pytest -k add -v (only selects tests that their names' contain the word 'add')