from actors import Entity, Pawns


class DungeonEntitySpawner:
    """Handles spawning of all entities (player and NPCs) for a dungeon."""

    def __init__(self):
        """Initialize the spawner and create an empty Pawns container."""
        self._pawns = Pawns()

    @property
    def pawns(self) -> Pawns:
        """Return the Pawns container for this spawner."""
        return self._pawns

    def spawn_player(self, *, x: int, y: int) -> None:
        """Add the player entity to the Pawns container."""
        self._pawns.player = Entity(char="@", color=(255, 255, 255), x=x, y=y)

    def spawn_npc(self, *, x: int, y: int) -> None:
        """Add an NPC entity to the Pawns container."""
        self._pawns.add_npc(Entity(char="O", color=(255, 255, 0), x=x, y=y))
