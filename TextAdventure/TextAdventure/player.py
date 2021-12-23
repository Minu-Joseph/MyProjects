import random 
import items, world,sounds
 
class Player():
    def __init__(self):
        self.currentWpn = None
        self.inventory = [items.ChainSaw(), items.SpikedBat(),items.Sword(),items.CrossBow(),items.ShortPortions(),items.ShortPortions(),items.ShortPortions()] #Inventory on startup
        self.hp = 100 # Health Points
        self.maxHp = 100
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.level =  1

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
         if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                if self.currentWpn is not None:
                     best_weapon = self.currentWpn
                else :
                    best_weapon = i
        sounds.attack()
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)

    def equip(self):
        print("\n These are the weapons you currently possess. \n ")
        weapon_list = []
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapon_list.append(item)
        i = 1
        for weapon in weapon_list:
            print(i, ". ", weapon.name, sep='')
            i += 1
        while True:
            itemChoice = int(input("""\nSelect the weapon you want to equip""")) - 1
            if itemChoice not in range(0, len(weapon_list)):
                print("\nInvalid weapon choice")
                sounds.invalidCode()
                continue
            break
        print("\n")
        print(weapon_list[itemChoice].name, "equipped.\n")
        self.currentWpn = weapon_list[itemChoice]

    def heal(self):
        print("\nThese are the potions you currently possess.\n")
        potion_list = []
        # item choose(self, items. Potions)
        for potion in self.inventory:
            if isinstance(potion, items.Portions):
                if potion.amt <= 0:
                    self.inventory.remove(potion)
                    continue
                else:
                    potion_list.append(potion)

        i = 1
        for potion in potion_list:
            print(i, ". ", potion.name, sep='')
            i += 1
        while True:
            if len(potion_list) == 0:
                print("You have no potions.")
                return None

            itemChoice = int(input("""\nSelect a potion: """)) - 1

            if itemChoice not in range(0, len(potion_list)):
                print("\nInvalid choice")
                sounds.invalidCode()
                continue
            break

        self.healToPlayer(itemChoice, potion_list)

    def healToPlayer(self, itemChoice, potionList):
        chosenPotion = potionList[itemChoice]

        print('\n You were healed for {} hp '.format(chosenPotion.health))
        self.hp = self.hp + chosenPotion.health
        print('hp',self.hp)
        chosenPotion.amt = chosenPotion.amt - 1
        if chosenPotion.amt == 0:
            self.inventory.remove(chosenPotion)
        sounds.drink()
        if self.maxHp < self.hp:
            self.hp = self.maxHp