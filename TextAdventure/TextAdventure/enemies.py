class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Ghoul(Enemy):
    def __init__(self):
        super().__init__(name="Ghoul", hp=10, damage=2)
 
class Bursters(Enemy):
    def __init__(self):
        super().__init__(name="Bursters", hp=30, damage=15)

class Exploders(Enemy):
    def __init__(self):
        super().__init__(name="Exploders", hp=20, damage=10)


class Hazmat(Enemy):
    def __init__(self):
        super().__init__(name="Hazmat", hp=25, damage=15)

class VamphireSquid(Enemy):
    def __init__(self):
        super().__init__(name="VamphireSquid", hp=25, damage=15)

class Wobbegong(Enemy):
    def __init__(self):
        super().__init__(name="Wobbegong", hp=20, damage=10)


class SeaSerpent(Enemy):
    def __init__(self):
        super().__init__(name="SeaSerpent", hp=30, damage=15)

class BlobFish(Enemy):
    def __init__(self):
        super().__init__(name="BlobFish", hp=10, damage=2)

class Zaratan(Enemy):
    def __init__(self):
        super().__init__(name="Zaratan", hp=25, damage=15)

class MummyLord(Enemy):
    def __init__(self):
        super().__init__(name="MummyLord", hp=20, damage=10)


class Oinoloth(Enemy):
    def __init__(self):
        super().__init__(name="Oinoloth", hp=30, damage=15)

class Gynosphinx(Enemy):
    def __init__(self):
        super().__init__(name="Gynosphinx", hp=10, damage=2)