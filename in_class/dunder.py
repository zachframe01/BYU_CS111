# the blocks or code from this file should be pasted into the 
# python interpreter to see and understand the results

# __str__ usage
from fractions import Fraction
one_third = 1/3
one_half = Fraction(1, 2)
print(one_third)
print(one_half)
str(one_third) 
str(one_half)
print(f"{one_half} > {one_third}")
# __str__ usage end

# Custom __str__ behavior
class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Lamb named " + self.name


lil = Lamb("Lil lamb")
str(lil)
print(lil)
lil
# Custom __str__ behavior end

# __repr__ usage
from fractions import Fraction
one_third = 1/3
one_half = Fraction(1, 2)
one_third
one_half
repr(one_third)
repr(one_half)
eval(repr(one_half))
# __repr__ usage end

# Custom __repr__ behavior
class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Lamb named " + self.name
    def __repr__(self):
        return f"Lamb('{self.name}')"

lil = Lamb("Lil lamb")
print(lil)
print(repr(lil))
lil
# Custom __repr__ behavior end
