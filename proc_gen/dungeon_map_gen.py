from __future__ import annotations

import random
from typing import Iterator, Tuple

import tcod

from actors import Pawns
from game_map import GameMap
from graphical_block_characters import GraphicalBlockCharacters as Graphics
from proc_gen.dungeon_spawn_gen import DungeonEntitySpawner
from rectangular_room import RectangularRoom


def generate_dungeon(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
) -> Tuple[GameMap, Pawns, Tuple[int, int]]:
    """Generate a new dungeon map.

    Returns:
        A tuple of (GameMap, Pawns, starting_position) where starting_position is (x, y).
    """
    dungeon = GameMap(map_width, map_height)
    starting_position = (0, 0)

    for _ in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        # "RectangularRoom" class makes rectangles easier to work with.
        new_room = RectangularRoom(x, y, room_width, room_height)

        # Run through the other rooms and see if they intersect with this one.
        if any(new_room.intersects(other_room) for other_room in dungeon.rooms):
            continue  # This room intersects, so go to the next attempt.
        # If there are no intersections then the room is valid.

        # Dig out this rooms inner area.
        dungeon.tiles[new_room.inner] = Graphics.floor_tile()

        if len(dungeon.rooms) == 0:
            # The first room, where the player starts.
            starting_position = new_room.center
        else:
            # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in tunnel_between(dungeon.rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = Graphics.floor_tile()

        # Finally, append the new room to the list.
        dungeon.rooms.append(new_room)

    pawns = DungeonEntitySpawner().spawn_pawns()

    return dungeon, pawns, starting_position

def tunnel_between(
    start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y
