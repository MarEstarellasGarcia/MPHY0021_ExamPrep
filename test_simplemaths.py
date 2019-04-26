import pytest
from simplemaths.simplemaths import SimpleMaths as sm
from pytest import raises
#
#class TestSimpleMaths():
##   pass
def test_wrong_input():
    with raises(TypeError):
        sm.only_accept_integers(5.2)


def test_square():
    sm(2).square()
    answer = 4
    assert sm(2).square() == answer


def test_power():
    sm(2).power(3)
    answer = 8
    assert sm(2).power(3) == answer
    
def test_factorial():
    assert sm(0).factorial() == 1
    assert sm(3).factorial() == 6
    
    
def test_oddOrEven():
    assert sm(2).odd_or_even() == "Even"
    assert sm(3).odd_or_even() == "Odd"
        
def test_sqrt():
    assert sm(16).square_root() == 4    