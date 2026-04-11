from actors import Entity, Pawns
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


def spawn_pawns() -> Pawns:
    """Return a Pawns instance containing the player character and all NPCs."""
    pawns = Pawns()
    pawns.player = _spawn_player_actor()
    pawns.add_npc(_spawn_npc_actor())

    return pawns

def _spawn_player_actor() -> Entity:
    """Return the entity representing the player character."""
    return Entity("@", (255, 255, 255), 0, 0)

def _spawn_npc_actor() -> Entity:
    """Return an entity controlled by the game's AI as non-player characters (NPCs)."""
    return Entity("O", (255, 255, 0), int(WINDOW_WIDTH / 2 - 5), int(WINDOW_HEIGHT / 2))
