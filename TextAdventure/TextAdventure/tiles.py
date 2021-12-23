import items, enemies, actions, world,sounds


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You wake up cold and alone surrounded by darkness. You react to the strong the pungent smell of pine and sap. 
        As your eyes adjust to the darkness you realize you're surrounded by dark..You lost the way in forest !!
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy attack and  made  {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive() :
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Equip(),actions.Heal()]
        else:
            return self.adjacent_moves()


class EmptyDarkPath(MapTile):
    def intro_text(self):
        return """
        Another darker side  of the forest . Move forward with hope.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class GhoulRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ghoul())

    def intro_text(self):
        if self.enemy.is_alive():

            return """
            A giant ghoul jumps down from a tree  in front of you and starts to bite you!
            """
        else:
            return """
            The corpse of a dead ghoul lies  on the ground.
            """


class BurstersRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bursters())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.horror()
            return """
             A burster  jumps  in front of you bursting with blood and fire !
             """
        else:
            return """
             The corpse of a dead burster is on the ground.
             """

class LeaveForestRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!!
         .....Level 1 Completed...... You have Max HP now.....          
        You reached outside the forest !!! An ocean is in front to cross !!! Try to cross the ocean.
        A boat is in shore . Grab the boat and boe in through the sea.         
        """

    def modify_player(self, player):
        player.victory = True
        #player.level = player.level + 1

class HazmatRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Hazmat())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.hazmatSound()
            return """
             A Hazmat  jumps down in front of you and tries to punch you !
             """
        else:
            return """
             The corpse of a dead Hazmat is on the ground.
             """


class ExplodersRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Exploders())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             An Exploder zombie  throws explosive gas upon you !!!
             """
        else:
            return """
             The corpse of a dead Exploder is on the ground.
             """

class StartingShore(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are now in the  boat !! Boe the boat 
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class EmptyOceanWay(MapTile):
    def intro_text(self):
        return """
        The sea is flowing silently  . Move forward as fast as you can.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class VamphireSquidRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.VamphireSquid())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Vamphire Squid tries to eat you with their sticky filament tentacles 
             """
        else:
            return """
             The corpse of a dead Vamphire Squid floats  on the sea."""

class WobbegongRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wobbegong())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Wobbegong shark pulls you to sea and can easily bite a hand holding onto their tail with their sharp teeth
              
             """
        else:
            return """
             The corpse of a dead shark  floats  on the sea.
             """


class SeaSerpentRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SeaSerpent())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A sea serpent is coming to bite you !!!

             """
        else:
            return """
             The corpse of a dead serpent  floats  on the sea.
             """
class BlobFishRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BlobFish())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             You tries to catch a fish from sea when you are hungry and a blob fish gets caught in your net !!! Attack.. 

             """
        else:
            return """
             The corpse of a dead blob fish   on the sea.
             """


class LeaveOceanRoom(MapTile):
    def intro_text(self):
        return """
        You crossed the sea safely ...  Level 2 Completed .......          
        You have Max HP now.....   
        A desert is in front of  you !! Take some rest !!  You are in your final level of the game.         
        """

    def modify_player(self, player):
        player.victory = True


class StartingPoint(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You reached the desert  !! Take some rest and start walking through the desert to find the way out. 
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptyDesertWay(MapTile):
    def intro_text(self):
        return """
        The desert  is filled with wind and sand  . There is a chance of storm coming.
         Walk fastly so that you reach the destination . 
         There is truck waiting at the end which gets to to your home.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class GynosphinxRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Gynosphinx())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Gynosphinx is coming through the wind and attacks you from the top. 
             """
        else:
            return """
             The corpse of a dead Gynosphinx  lies in the desert ."""


class OinolothRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Oinoloth())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Oinoloth tries to scare you !!

             """
        else:
            return """
             The corpse of a dead Oinoloth  lies in the desert .
             """


class MummyLordRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MummyLord())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A MummyLord   comes and stands in front of you  !!!

             """
        else:
            return """
             The corpse of a dead MummyLord  floats on the desert.
             """


class ZaratanRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zaratan())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Zaratan monster  comes and stands in front of you after heavy wind and storm   !!! 

             """
        else:
            return """
             The corpse of a dead monster   on the desert 
             """


class LeaveDesertRoom(MapTile):
    def intro_text(self):
        return """
        Hurray !!!! Here is the truck which  drive to your home...   

        Game Completed !!!!       
        """

    def modify_player(self, player):
        player.victory = True