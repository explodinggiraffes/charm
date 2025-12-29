from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


MOVE_KEYS = {
    # Arrow keys.
    tcod.event.KeySym.UP: (0, -1),
    tcod.event.KeySym.DOWN: (0, 1),
    tcod.event.KeySym.LEFT: (-1, 0),
    tcod.event.KeySym.RIGHT: (1, 0),
    tcod.event.KeySym.HOME: (-1, -1),
    tcod.event.KeySym.END: (-1, 1),
    tcod.event.KeySym.PAGEUP: (1, -1),
    tcod.event.KeySym.PAGEDOWN: (1, 1),
    # Numpad keys.
    tcod.event.KeySym.KP_1: (-1, 1),
    tcod.event.KeySym.KP_2: (0, 1),
    tcod.event.KeySym.KP_3: (1, 1),
    tcod.event.KeySym.KP_4: (-1, 0),
    tcod.event.KeySym.KP_6: (1, 0),
    tcod.event.KeySym.KP_7: (-1, -1),
    tcod.event.KeySym.KP_8: (0, -1),
    tcod.event.KeySym.KP_9: (1, -1),
    # Vi keys.
    tcod.event.KeySym.H: (-1, 0),
    tcod.event.KeySym.J: (0, 1),
    tcod.event.KeySym.K: (0, -1),
    tcod.event.KeySym.L: (1, 0),
    tcod.event.KeySym.Y: (-1, -1),
    tcod.event.KeySym.U: (1, -1),
    tcod.event.KeySym.B: (-1, 1),
    tcod.event.KeySym.N: (1, 1),
}

class EventHandler(tcod.event.EventDispatch[Action]):
    """Translates TCOD events to Actions.

    Handles keyboard input and quit events, supporting 8-directional movement
    via arrow keys, numpad, and vi-keys. Returns Action objects that can be
    performed by entities in the game.
    """
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        """Called when a keyboard key is pressed or repeated."""
        action: Optional[Action] = None

        key = event.sym
        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = MovementAction(dx, dy)
        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()  # TODO: Rename to GameExitAction

        return action

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        """Called when the termination of the game is requested."""
        raise SystemExit()
