from typing import List

from actors import Entity
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


def spawn_pawns() -> List[Entity]:
    """Return a list of all pawns: the player character, as well as all NPCs."""
    player = _spawn_player_actor()
    npc = _spawn_pawn()

    entities = [player, npc]

    return entities

def _spawn_player_actor() -> Entity:
    """Return the entity representing the player character."""
    return Entity("@", (255, 255, 255), 0, 0)

def _spawn_pawn() -> Entity:
    """Return an entity controlled by the game's AI as non-player characters (NPCs)."""
    return Entity("O", (255, 255, 0), int(WINDOW_WIDTH / 2 - 5), int(WINDOW_HEIGHT / 2))
