from constants import MAP_HEIGHT, MAP_WIDTH, ROOMS_MAX, ROOM_SIZE_MAX, ROOM_SIZE_MIN
from proc_gen import generate_dungeon, spawn_pawns


class World:
    """A container for all the levels/maps that make up your game."""
    def __init__(self):
        self.current_map = None

    def create_dungeon(self) -> None:
        """Generate a new dungeon map and populate self.current_map."""
        self.current_map, starting_position = generate_dungeon(
            max_rooms=ROOMS_MAX,
            room_min_size=ROOM_SIZE_MIN,
            room_max_size=ROOM_SIZE_MAX,
            map_width=MAP_WIDTH,
            map_height=MAP_HEIGHT,
        )
        pawns = spawn_pawns()
        self.current_map.entities = [pawns.player] + pawns.npcs
        self.current_map.player = pawns.player
        self.current_map.player.x, self.current_map.player.y = starting_position
