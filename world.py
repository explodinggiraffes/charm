from constants import MAP_HEIGHT, MAP_WIDTH, ROOMS_MAX, ROOM_SIZE_MAX, ROOM_SIZE_MIN
from game_map import GameMap
from procgen import generate_dungeon


class World:
    """A container for all the levels/maps that make up your game."""

    @staticmethod
    def create_dungeon() -> GameMap:
        """Generate and return a new dungeon map with the player positioned in the first room."""
        return generate_dungeon(
            max_rooms=ROOMS_MAX,
            room_min_size=ROOM_SIZE_MIN,
            room_max_size=ROOM_SIZE_MAX,
            map_width=MAP_WIDTH,
            map_height=MAP_HEIGHT,
        )
