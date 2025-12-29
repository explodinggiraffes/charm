from typing import List

import numpy as np
from tcod.console import Console

from graphical_block_characters import SHROUD, GraphicalBlockCharacters as Graphics
from rectangular_room import RectangularRoom


class GameMap:
    """A game map made up of rooms that contain entities such as players, enemies, items, etc."""
    def __init__(self, width: int, height: int):
        # Map dimensions
        self.width = width
        self.height = height

        # Room layout
        self.rooms: List[RectangularRoom] = []

        # Tile data and visibility tracking
        self.tiles = np.full((width, height), fill_value=Graphics.wall_tile(), order="F")
        self.visible = np.full((width, height), fill_value=False, order="F")   # Tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the player has seen before

        # Entity tracking
        self.entities = None
        self.player = None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map, False if not."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """
        console.rgb[0 : self.width, 0 : self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=SHROUD
        )
