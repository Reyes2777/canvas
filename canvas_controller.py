class CanvasController:

    def __init__(self, wide_canvas: int, height_canvas: int):
        self.wide_canvas = wide_canvas
        self.height_canvas = height_canvas
        self._create_board_canvas()

    def _create_board_canvas(self):
        top = '-' * (self.wide_canvas + 2)
        height = ('\n|' + ' ' * self.wide_canvas + '|') * self.height_canvas
        self.canvas = top + height + '\n' + top
