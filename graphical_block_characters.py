import tcod


class GraphicalBlockCharacters:
    """The graphical block characters used to create the game map, entities, etc.
    Includes the main tileset.
    TODO:
    1. Individual tiles -- refactor tile_types.py to this class?
    2. Add tileset loader functionality -- the game can support multiple tilesets?
    """
    def __init__(self):
        # TODO: Use a different tileset?
        # https://dwarffortresswiki.org/index.php/DF2014:Tileset_repository
        self.tileset = tcod.tileset.load_tilesheet(
            "assets/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
        tcod.tileset.procedural_block_elements(tileset=self.tileset)
