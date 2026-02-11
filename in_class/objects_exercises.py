"""
This class represents a player in a video game.
It tracks their name and health.
"""
class Player:
    """
    >>> player = Player("Mario")
    >>> player.name
    'Mario'
    >>> player.health
    100
    >>> player.damage(10)
    >>> player.health
    90
    >>> player.boost(5)
    >>> player.health
    95
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def damage(self, amount):
        self.health -= amount

    def boost(self, amount):
        self.health += amount

"""
Clothing is a class that represents pieces of clothing in a closet. It tracks
the color, category, and clean/dirty state.
"""
class Clothing:
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """
    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True

    def wear(self):
        self.is_clean = False

    def clean(self):
        self.is_clean = True


