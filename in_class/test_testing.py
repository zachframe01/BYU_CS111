import testing, pytest 

def test_square_valid():
    assert testing.square(3.1415) == 9.86902225
    assert testing.square(5) == 25
    assert testing.square(-10) == 100


def test_square_root_raises_ValueError():
    with pytest.raises(ValueError):
        testing.square_root(-16)

def test_square_root_valid():
    assert testing.square_root(9) == 3
    assert testing.square_root(126.5625) == 11.25

def test_add_floats():
    assert testing.add_floats(0.1,0.2) == pytest.approx(0.3) 

def test_div_floats():
    # your code here
    pass

# what other test_ function should you create for div_floats? 
# create it here