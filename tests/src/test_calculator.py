from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520

def test_subtract():
    assert cal.subtract(4,1) == 3
    assert cal.subtract(23,22) == 1

def test_multify():
    assert cal.multify(2,3) == 6
    assert cal.multify(200,0) == 0


