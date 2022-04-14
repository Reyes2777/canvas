class CanvasController:

    def __init__(self, wide_canvas: int, height_canvas: int):
        self.wide_canvas = wide_canvas
        self.height_canvas = height_canvas
        self._create_board_canvas()

    @property
    def wide_canvas(self):
        return self._wide_canvas

    @wide_canvas.setter
    def wide_canvas(self, value):
        if not type(value) == int:
            raise Exception('Value wide should Integer')
        if not value > 0:
            raise Exception('Value wide should more that 0')
        self._wide_canvas = value

    @property
    def height_canvas(self):
        return self._height_canvas

    @height_canvas.setter
    def height_canvas(self, value):
        if not type(value) == int:
            raise Exception('Value height should Integer')
        if not value > 0:
            raise Exception('Value height should more that 0')
        self._height_canvas = value

    def _create_board_canvas(self):
        top = '-' * (self.wide_canvas + 2)
        height = ('\n|' + ' ' * self.wide_canvas + '|') * self.height_canvas
        self.canvas = top + height + '\n' + top
