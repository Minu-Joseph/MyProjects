# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class SpikedBat(Weapon):
    def __init__(self):
        super().__init__(name="SpikedBat",
                         description="A Spiked Bat, 10 times better than a normal bat.",
                         value=0,
                         damage=25)
 
class ChainSaw(Weapon):
    def __init__(self):
        super().__init__(name="ChainSaw",
                         description="A ChainSaw with some power. Somewhat more powerful than a spiked bat.",
                         value=10,
                         damage=20)
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A normal Sword.",
                         value=1,
                         damage=1)

class CrossBow(Weapon):
    def __init__(self):
        super().__init__(name="CrossBow",
                         description="A CrossBow.",
                         value=5,
                         damage=25)

class SpearGun(Weapon):
    def __init__(self):
        super().__init__(name="SpearGun",
                         description="A SpearGun.",
                         value=5,
                         damage=25)

class Spear(Weapon):
    def __init__(self):
        super().__init__(name="Spear",
                         description="A Spear.",
                         value=5,
                         damage=20)

class Harpoon(Weapon):
    def __init__(self):
        super().__init__(name="Harpoon",
                         description="A Harpoon.",
                         value=5,
                         damage=10)

class Rod(Weapon):
    def __init__(self):
        super().__init__(name="Rod",
                         description="A Rod.",
                         value=5,
                         damage=5)


class RemoteBomb(Weapon):
    def __init__(self):
        super().__init__(name="RemoteBomb",
                         description="A RemoteBomb.",
                         value=5,
                         damage=25)
class WulfrumBow(Weapon):
    def __init__(self):
        super().__init__(name="WulfrumBow",
                         description="A WulfrumBow.",
                         value=5,
                         damage=15)

class Stones(Weapon):
    def __init__(self):
        super().__init__(name="Stones",
                         description="A Stones.",
                         value=5,
                         damage=10)
class Portions(Item):
    def __init__(self, name, description, value,amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)

class ShortPortions(Portions):
    def __init__(self):
        super().__init__(name="Small Potion",
                         description="A Small Potion",
                         value=5,
                         amt =1 ,
                         health=25)

