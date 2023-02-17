from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1,3) == 4
    assert cal.add(500,20) == 520
