from constants import MAP_HEIGHT, MAP_WIDTH, ROOMS_MAX, ROOM_SIZE_MAX, ROOM_SIZE_MIN
from game_map import GameMap
from proc_gen import generate_dungeon


class World:
    """A container for all the levels/maps that make up your game."""
    def __init__(self):
        self.current_map = None

    def create_dungeon(self) -> None:
        """Generate a new dungeon map and populate self.current_map."""
        self.current_map = generate_dungeon(
            max_rooms=ROOMS_MAX,
            room_min_size=ROOM_SIZE_MIN,
            room_max_size=ROOM_SIZE_MAX,
            map_width=MAP_WIDTH,
            map_height=MAP_HEIGHT,
        )
