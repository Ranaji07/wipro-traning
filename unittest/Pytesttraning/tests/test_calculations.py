import pytest

from src.calculations import Calculations
class TestCalculations:

    calc = Calculations()
    # @pytest.fixture(scope='class', autouse=True )
    # def setup(self):
    #     print('Fixture')

# @pytest.fixture()
# def setUp(self):
#     return calc
@pytest.mark.parametrize("n1, n2, exval",[(5, 5, 10), (-5, -5, -10), (0, 5, 5) ])


def test_add(self, n1, n2, exval):
    res = self.calc.add(n1, n2)
    assert res == exval, 'Addition Err'

def test_mul(self,):
    res = self.calc.mul(n1=10, n2=5)
    assert res == 50, 'Mul Err'

def test_div(self):
    res = self.calc.div(n1=10, n2=0)
    assert res == 0, 'Div Err'

def test_ne(self):
    res = self.calc.ne(n1=10, n2=5)
    assert res == True, 'NE'

# def test_diverr(self):
#     with pytest.raises(ZeroDivisionError):
#         self.calc.div(n1=10, n2=0)