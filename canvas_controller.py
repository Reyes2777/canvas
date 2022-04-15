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

    def _draw_line_horizontal(self, axis_x1: int, axis_x2: int, axis_y: int):
        long_line = axis_x2 - (axis_x1 - 1)
        stop = axis_x1 + long_line
        self.list_lines_canvas[axis_y] = self.list_lines_canvas[axis_y][:axis_x1] + ('x' * long_line) + \
            self.list_lines_canvas[axis_y][stop:]

    def _draw_line_vertical(self, axis_y1: int, axis_y2: int, axis_x: int):
        for value in range(axis_y1, axis_y2 + 1):
            self.list_lines_canvas[value] = self.list_lines_canvas[axis_y2][:axis_x] + 'x' + self.list_lines_canvas[value][
                                                                                             axis_x + 1:]

    def _draw_manage_errors(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        if not type(axis_x1) is int or not type(axis_x2) is int or not type(axis_y1) is int or not type(axis_y2) is int:
            raise Exception('All values should be integers')
        if axis_x1 > self.wide_canvas or axis_x2 > self.wide_canvas or axis_y1 > self.height_canvas or \
                axis_y2 > self.height_canvas:
            raise Exception('Line out of area canvas')

    def draw_line(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        self._draw_manage_errors(axis_x1=axis_x1, axis_y1=axis_y1, axis_x2=axis_x2, axis_y2=axis_y2)
        if axis_x1 == axis_x2:
            self._draw_line_vertical(axis_y1=axis_y1, axis_y2=axis_y2, axis_x=axis_x1)
        elif axis_y1 == axis_y2:
            self._draw_line_horizontal(axis_x1=axis_x1, axis_x2=axis_x2, axis_y=axis_y2)
        else:
            raise Exception('This app not draw diagonal lines')
        self._draw_canvas()

    def draw_square(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        self._draw_manage_errors(axis_x1=axis_x1, axis_y1=axis_y1, axis_x2=axis_x2, axis_y2=axis_y2)
        self._draw_line_vertical(axis_y1=axis_y1, axis_y2=axis_y2, axis_x=axis_x1)
        self._draw_line_vertical(axis_y1=axis_y1, axis_y2=axis_y2, axis_x=axis_x2)
        self._draw_line_horizontal(axis_x1=axis_x1, axis_x2=axis_x2, axis_y=axis_y1)
        self._draw_line_horizontal(axis_x1=axis_x1, axis_x2=axis_x2, axis_y=axis_y2)
        self._draw_canvas()

