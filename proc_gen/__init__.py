"""Procedural generation module for game maps and entities."""

from proc_gen.dungeon_map_gen import (
    generate_dungeon,
    tunnel_between,
)
from proc_gen.dungeon_spawn_gen import DungeonEntitySpawner

__all__ = [
    "generate_dungeon",
    "DungeonEntitySpawner",
    "tunnel_between",
]
