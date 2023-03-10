from app.src.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520
    assert cal.add(3,5) == 8
    assert cal.add(2,10) == 12

def test_subtract():
    assert cal.subtract(4,1) == 3
    assert cal.subtract(23,22) == 1
    assert cal.subtract(5,2) == 3

def test_multifly():
    assert cal.multifly(2,3) == 6
    assert cal.multifly(50,0) == 0
    assert cal.multifly(2,2) == 4
    assert cal.multifly(2,7) == 14

def test_divide_():
    assert cal.divide(100,20) == 5
    assert cal.divide(6,3) == 2
    assert cal.divide(2,0) == 0
    assert cal.divide(4,2) == 2
    assert cal.divide(100,50) == 2
    assert cal.divide(10,0) == 0

