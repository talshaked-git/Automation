from source.accum import Accumulator
import pytest

@pytest.fixture # default scope is 'function'
def accum_global():
    return Accumulator()