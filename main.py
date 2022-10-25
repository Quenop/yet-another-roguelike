import sys
import os
import glob

import tcod
import tcod.event

from action import EscapeAction, MoveAction
from input_handlers import HandleKeys

def main():

    # Screen
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 55

    self_x = int(SCREEN_WIDTH / 2)
    self_y = int(SCREEN_HEIGHT / 2)

    # Initialization
    tileset = tcod.tileset.load_tilesheet(FONT_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD)

    handle_keys = HandleKeys()

    # Perephirals
    key = tcod.Key()
    mouse = tcod.Mouse()

    ## Game logic ##
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset = tileset,
        title = "S1MPLE R0GUELIKE",
        vsync = True
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order = "F")
        while True:
            root_console.print(x = self_x, y = self_y, string = "@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = handle_keys.dispatch(event)

                if action is None:
                    continue
                if isinstance(action, MoveAction):
                    self_x += action.dx
                    self_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

# Data
DATA_FOLDER = "data"
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")



if __name__ == "__main__":
    main()
