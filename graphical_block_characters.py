from typing import Tuple

import numpy as np
import tcod


# Tile color struct compatible with Console.tiles_rgb.
TILE_GRAPHIC_COLORS = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),      # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
TILE_DATA = np.dtype(
    [
        ("walkable", bool),              # True if this tile can be walked over.
        ("transparent", bool),           # True if this tile doesn't block FOV.
        ("dark", TILE_GRAPHIC_COLORS),   # Graphics for when this tile is not in FOV.
        ("light", TILE_GRAPHIC_COLORS),  # Graphics for when the tile is in FOV.
    ]
)

# Unexplored, unseen tiles.
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=TILE_GRAPHIC_COLORS)


class GraphicalBlockCharacters:
    """The graphical block characters used to create the game map, entities, etc.
    Includes the main tileset as well as individual tile graphics.
    """
    def __init__(self):
        self.tileset = tcod.tileset.load_tilesheet(
            "assets/Md_curses_16x16.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
        tcod.tileset.procedural_block_elements(tileset=self.tileset)

    @staticmethod
    def floor_tile() -> np.ndarray:
        """Returns a floor tile."""
        return GraphicalBlockCharacters.__new_tile(
            walkable=True,
            transparent=True,
            dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
            light=(ord(" "), (255, 255, 255), (200, 180, 50)),
        )

    @staticmethod
    def wall_tile() -> np.ndarray:
        """Returns a wall tile."""
        return GraphicalBlockCharacters.__new_tile(
            walkable=False,
            transparent=False,
            dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
            light=(ord(" "), (255, 255, 255), (130, 110, 50)),
        )

    @staticmethod
    def __new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    ) -> np.ndarray:
        """Helper method for defining individual tile types."""
        return np.array((walkable, transparent, dark, light), dtype=TILE_DATA)
