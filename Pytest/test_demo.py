import pytest
a=6
@pytest.mark.skip(reason="empty code")
def test_sample_one():
    print("Hai")
@pytest.mark.smoke
@pytest.mark.skipif(a>5,reason="value above 5")
def test_sample1():
    # print("Welcome")
    a=10
    b=10
    assert a==b
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="expected to pass")
def test_sample2():
    # print("Pytest")
    a=5
    b=10
    assert a<b
@pytest.mark.regression
@pytest.mark.xfail(reason="assert is wrong")
def test_sample3():
    a="yuvaraj"
    b="yuvara"
    assert a.__eq__(b)

@pytest.mark.parametrize("test_input,expected",[(1,3),(3,5),(5,7)])
def test_addition(test_input,expected):
    assert test_input+2==expected