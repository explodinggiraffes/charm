from typing import List

from actors.entity import Entity
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


class World:
    """A container for all the levels/maps that make up your game.
    It handles the streaming of levels and the spawning (creation) of dynamic entities and actors.
    """

    @staticmethod
    def spawn_actor() -> Entity:
        """Return the entity representing the player character."""
        return Entity("@", (255, 255, 255), 0, 0)

    @staticmethod
    def spawn_pawn() -> Entity:
        """Return an entity controlled by the game's AI as non-player characters (NPCs)."""
        # FIXME: The map generator should be determining the location of NPC(s), as this method can place the entity
        # inside of a wall, etc.
        return Entity("O", (255, 255, 0), int(WINDOW_WIDTH / 2 - 5), int(WINDOW_HEIGHT / 2))

    @staticmethod
    def spawn_pawns() -> List[Entity]:
        """Return a list of all pawns: the player character, as well as all NPCs."""
        player = World.spawn_actor()
        npc = World.spawn_pawn()

        entities = [player, npc]
        return entities
