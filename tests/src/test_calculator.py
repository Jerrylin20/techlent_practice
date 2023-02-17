from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520

def test_subtract():
    assert cal.subtract(3,1) == 2
    assert cal.subtract(5,2) == 3

def test_multify():
    assert cal.multify(2,3) == 6
    assert cal.multify(50,0) == 0

def test_divide():
    assert cal.divide(4,2) == 2
    assert cal.divide(100,50) == 2



