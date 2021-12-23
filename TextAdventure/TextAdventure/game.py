import os.path

import world
from player import Player
import items
count = 1
def play():

    global count
    while count <= 3:
        world.load_tiles('map.txt')
        player = Player()
        if count == 2:
            world.load_tiles('map2.txt')
            player.inventory = [items.Harpoon(), items.Spear(),items.SpearGun(),items.Rod(),items.ShortPortions(),items.ShortPortions(),items.ShortPortions()]
            player.victory = False
            player.hp = 100  # Health Points
            player.maxHp = 100
        if count == 3:
            world.load_tiles('map3.txt')
            player.inventory = [items.Stones(), items.RemoteBomb(),items.WulfrumBow(),items.ShortPortions(),items.ShortPortions(),items.ShortPortions()]
            player.victory = False
            player.hp = 100  # Health Points
            player.maxHp = 100
        # These lines load the starting room and display the text
        room = world.tile_exists(player.location_x, player.location_y)
        print(room.intro_text())
        while player.is_alive() and not player.victory:
            room = world.tile_exists(player.location_x, player.location_y)
            room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                print("Choose an action:\n")
                available_actions = room.available_actions()
                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
        if player.is_alive() and player.victory:
                count = count + 1
                continue

if __name__ == "__main__":

    play()

