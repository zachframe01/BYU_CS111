import pytest, lab_section

# def test_square_valid():
#     assert testing.square(3.1415) == 9.86902225
#     assert testing.square(5) == 25
#     assert testing.square(-10) == 100

def test_add_valid(): 
    assert lab_section.add(2) == 4
    assert lab_section.add(7)==14
    assert lab_section.add(8) == 16

def test_sub_valid():
    assert lab_section.sub(7) == 0
    assert lab_section.sub(9) == 0
    assert lab_section.sub(14) == 0


