from actors import Entity, Pawns
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


def spawn_pawns() -> Pawns:
    """Return a Pawns instance containing the player character and all NPCs."""
    pawns = Pawns()
    pawns.player = spawn_player_actor()
    pawns.add_npc(spawn_npc_actor())

    return pawns

def spawn_player_actor() -> Entity:
    """Return the entity representing the player character."""
    return Entity(char="@", color=(255, 255, 255), x=0, y=0)

def spawn_npc_actor() -> Entity:
    """Return an entity controlled by the game's AI as non-player characters (NPCs)."""
    return Entity(char="O", color=(255, 255, 0), x=int(WINDOW_WIDTH / 2 - 5), y=int(WINDOW_HEIGHT / 2))
