class CanvasController:

    def __init__(self, wide_canvas: int, height_canvas: int):
        self.wide_canvas = wide_canvas
        self.height_canvas = height_canvas
        self.canvas = None
        self.list_lines_canvas = []
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

    def _draw_canvas(self):
        self.canvas = ''
        for line in self.list_lines_canvas:
            self.canvas += line + '\n'

    def _create_board_canvas(self):
        top = '-' * (self.wide_canvas + 2)
        self.list_lines_canvas.append(top)
        self.list_lines_canvas.append(top)
        for x in range(0, self.height_canvas):
            self.list_lines_canvas.insert(-1, f'|{self.wide_canvas * " "}|')
        self._draw_canvas()

    def _draw_line_horizontal(self, x1, x2, y2):
        long_line = x2 - (x1 - 1)
        stop = x1 + long_line
        self.list_lines_canvas[y2] = self.list_lines_canvas[y2][:x1] + ('x' * long_line) +\
            self.list_lines_canvas[y2][stop:]

    def _draw_line_vertical(self, y1, y2, x1):
        for value in range(y1, y2 + 1):
            self.list_lines_canvas[value] = self.list_lines_canvas[y2][:x1] + 'x' + self.list_lines_canvas[value][
                                                                                    x1 + 1:]

    def draw_line(self, x1, y1, x2, y2):
        if x1 == x2:
            self._draw_line_vertical(y1=y1, y2=y2, x1=x1)
        elif y1 == y2:
            self._draw_line_horizontal(x1=x1, x2=x2, y2=y2)
        self._draw_canvas()
