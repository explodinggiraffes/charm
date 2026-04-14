from actors import Entity, Pawns
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


class DungeonEntitySpawner:
    """Handles spawning of all entities (player and NPCs) for a dungeon."""

    def spawn_pawns(self) -> Pawns:
        """Return a Pawns instance containing the player character and all NPCs."""
        self._pawns = Pawns()
        self._pawns.player = self.spawn_player_actor()
        self._pawns.add_npc(self.spawn_npc_actor())

        return self._pawns

    def spawn_player_actor(self) -> Entity:
        """Return the entity representing the player character."""
        return Entity(char="@", color=(255, 255, 255), x=0, y=0)

    def spawn_npc_actor(self) -> Entity:
        """Return an entity controlled by the game's AI as non-player characters (NPCs)."""
        return Entity(char="O", color=(255, 255, 0), x=int(WINDOW_WIDTH / 2 - 5), y=int(WINDOW_HEIGHT / 2))
