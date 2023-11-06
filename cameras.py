from asciimatics.effects import Print
from asciimatics.renderers import ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    scenes = []

    effects = [
        Print(screen,
              StaticRenderer(images=["< Press SPACE to exit. >"]),
              screen.height - 2),

        Print(screen,
              ImageFile("anim/cctv.gif", screen.height - 4, colours=8),
              0, speed=1),
    ]
    scenes.append(Scene(effects))

    screen.play(scenes, stop_on_resize=True, repeat=False)

    screen.close()


def play_camera():
    while True:
        try:
            Screen.wrapper(demo)

            return
        except ResizeScreenError:
            pass


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
