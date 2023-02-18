from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520

def test_subtract():
    assert cal.subtract(4,1) == 3
    assert cal.subtract(23,22) == 1
    assert cal.subtract(5,2) == 3

def test_multifly():
    assert cal.multifly(2,3) == 6
    assert cal.multifly(50,0) == 0
    assert cal.multifly(2,2) == 4

def test_divide():
    assert cal.divide(4,2) == 2
    assert cal.divide(100,50) == 2


