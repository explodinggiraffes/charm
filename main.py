#!/usr/bin/env python3

import tcod

from constants import MAP_HEIGHT, MAP_WIDTH, ROOMS_MAX, ROOM_SIZE_MAX, ROOM_SIZE_MIN, WINDOW_HEIGHT, WINDOW_WIDTH
from engine import Engine
from entity import Entity
from procgen import generate_dungeon


def main() -> None:
    # TODO:
    # 1. Create a "tileset manager" that is used directly by the Engine class.
    #    Note in dot_hack, this was done in Engine.__init()___
    # 2. Update tileset: https://dwarffortresswiki.org/index.php/DF2014:Tileset_repository
    # Load the tileset.
    tileset = tcod.tileset.load_tilesheet(
        "assets/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    # TODO:
    # 1. Create an "entity manager" that spawns the player and NPCs that is used directly by the Engine class.
    #    Note in dot_hack, this was done in Engine.__init()___
    # Create the player and an NPC.
    player = Entity(int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2), "@", (255, 255, 255))
    npc = Entity(int(WINDOW_WIDTH / 2 - 5), int(WINDOW_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}

    # TODO:
    # 1. Create a "level manager" that creates game maps that is used directly by the Engine class.
    #    Note in dot_hack, this was done in Engine.__init()___
    # Create the game map.
    game_map = generate_dungeon(
        max_rooms=ROOMS_MAX,
        room_min_size=ROOM_SIZE_MIN,
        room_max_size=ROOM_SIZE_MAX,
        map_width=MAP_WIDTH,
        map_height=MAP_HEIGHT,
        player=player
    )

    # Create the engine and start the game.
    Engine(game_map=game_map, tileset=tileset, entities=entities, player=player)

if __name__ == "__main__":
    main()
