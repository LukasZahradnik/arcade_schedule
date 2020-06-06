import arcade
import state

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(state.x, state.y, 20, 20, (255, 0, 0, 255))

    def on_update(self, delta_time):
        import kid


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()