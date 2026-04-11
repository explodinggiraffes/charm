"""Procedural generation module for game maps and entities."""

from proc_gen.game_map_gen import (
    generate_dungeon,
    tunnel_between,
)
from proc_gen.pawn_gen import spawn_pawns

__all__ = [
    "generate_dungeon",
    "spawn_pawns",
    "tunnel_between",
]
