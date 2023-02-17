from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520

def test_subtract():
    assert cal.subtract(3,1) == 2
    assert cal.subtract(5,2) == 3

