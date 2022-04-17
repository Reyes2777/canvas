class CanvasController:
    """
    This is class manage all functionalities the canvas Board
    Attributes:
        wide_canvas (int): wide canvas board
        height_canvas (int): height canvas board
        canvas (str): is a string that is built as it is drawn on the canvas
        _list_lines_canvas (list): this is private attribute that contain a list that lines of canvas
                                   to write attr canvas

    Example:
        canvas = CanvasController(wide=20, height=4)
        canvas.draw_line(axis_x1=6, axis_y1=2, axis_x2=6, axis_y2=4)
        canvas.rectangle(axis_x1=6, axis_y1=2, axis_x2=16, axis_y2=4)
        canvas.bucket_fill(axis_x=10, axis_y=3, pattern='o')

    """

    def __init__(self, wide_canvas: int, height_canvas: int):
        """
        The constructor for Canvas Controller that when is initialized build area of canvas.
        Parameters:
            wide_canvas (str): wide of area canvas to build
            height_canvas (str): height of area canvas to build
        """
        self.wide_canvas = wide_canvas
        self.height_canvas = height_canvas
        self.canvas = None
        self._list_lines_canvas = []
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
        """
        This private function build attr canvas with contain in _list_lines_canvas
        Returns:
            attribute canvas of class
        """
        self.canvas = ''
        for line in self._list_lines_canvas:
            self.canvas += line + '\n'

    def _create_board_canvas(self):
        """
        This function is executed when class is instanced and build the canvas board
        """
        top = '-' * (self.wide_canvas + 2)
        self._list_lines_canvas.append(top)
        self._list_lines_canvas.append(top)
        for x in range(0, self.height_canvas):
            self._list_lines_canvas.insert(-1, f'|{self.wide_canvas * " "}|')
        self._draw_canvas()

    def _draw_line_horizontal(self, axis_x1: int, axis_x2: int, axis_y: int):
        """
        This function draw line horizontal in canvas board
        Parameters:
        axis_x1: point to start line
        axis_x2: point to finish line
        axis_y: point where locate in axis y line
        """
        long_line = axis_x2 - (axis_x1 - 1)
        stop = axis_x1 + long_line
        self._list_lines_canvas[axis_y] = self._list_lines_canvas[axis_y][:axis_x1] + ('x' * long_line) + \
                                          self._list_lines_canvas[axis_y][stop:]

    def _draw_line_vertical(self, axis_y1: int, axis_y2: int, axis_x: int):
        """
        This function draw line vertical in canvas board
        Parameters:
        axis_y1: point to start line
        axis_y2: point to finish line
        axis_x: point where locate in axis x line
        """
        for value in range(axis_y1, axis_y2 + 1):
            self._list_lines_canvas[value] = self._list_lines_canvas[value][:axis_x] + 'x' + \
                                             self._list_lines_canvas[value][axis_x + 1:]

    def _draw_manage_errors(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        if not type(axis_x1) is int or not type(axis_x2) is int or not type(axis_y1) is int or not type(axis_y2) is int:
            raise Exception('All values should be integers')
        if axis_x1 > self.wide_canvas or axis_x2 > self.wide_canvas or axis_y1 > self.height_canvas or \
                axis_y2 > self.height_canvas:
            raise Exception('Line out of area canvas')

    def draw_line(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        """
        This function draw line in canvas board
        Parameters:
        axis_x1: point to start in axis x
        axis_y1: point to start in axis y
        axis_x2: point to finish in axis x
        axis_y2: point to finish in axis y

        """
        self._draw_manage_errors(axis_x1=axis_x1, axis_y1=axis_y1, axis_x2=axis_x2, axis_y2=axis_y2)
        if axis_x1 == axis_x2:
            self._draw_line_vertical(axis_y1=axis_y1, axis_y2=axis_y2, axis_x=axis_x1)
        elif axis_y1 == axis_y2:
            self._draw_line_horizontal(axis_x1=axis_x1, axis_x2=axis_x2, axis_y=axis_y2)
        else:
            raise Exception('This app not draw diagonal lines')
        self._draw_canvas()

    def draw_rectangle(self, axis_x1: int, axis_y1: int, axis_x2: int, axis_y2: int):
        """
        This function draw rectangle in canvas board
        Parameters:
        axis_x1: point to start in axis x
        axis_y1: point to start in axis y
        axis_x2: point to finish in axis x
        axis_y2: point to finish in axis y
        """
        self._draw_manage_errors(axis_x1=axis_x1, axis_y1=axis_y1, axis_x2=axis_x2, axis_y2=axis_y2)
        self.draw_line(axis_y1=axis_y1, axis_y2=axis_y2, axis_x1=axis_x1, axis_x2=axis_x1)
        self.draw_line(axis_x1=axis_x1, axis_x2=axis_x2, axis_y1=axis_y1, axis_y2=axis_y1)
        self.draw_line(axis_y1=axis_y1, axis_y2=axis_y2, axis_x2=axis_x2, axis_x1=axis_x2)
        self.draw_line(axis_x1=axis_x1, axis_x2=axis_x2, axis_y1=axis_y2, axis_y2=axis_y2)

    def _fill_quarter_from_point(self, axis_x: int, axis_y: int, value_x: str, value_y: str, pattern: str = 'o'):
        """
        This private function solve problem to recursion when implement def bucket fill, fill by quarters from point
        """
        quarter = {'right': [1, 0], 'left': [-1, 0], 'up': [0, -1], 'down': [0, 1]}
        if self._list_lines_canvas[axis_y][axis_x] not in ('x', '|', '-'):
            self._list_lines_canvas[axis_y] = self._list_lines_canvas[axis_y][:axis_x] + pattern + \
                                              self._list_lines_canvas[axis_y][axis_x + 1:]
            self._fill_quarter_from_point(axis_x=axis_x + quarter[value_x][0],
                                          axis_y=axis_y + quarter[value_x][1],
                                          value_x=value_x, value_y=value_y)
            self._fill_quarter_from_point(axis_x=axis_x + quarter[value_y][0],
                                          axis_y=axis_y + quarter[value_y][1],
                                          value_x=value_x, value_y=value_y)
            self._draw_canvas()

# TODO: solve problem with limit recursion to don´t use fill by quarters
    def bucket_fill(self, axis_x: int, axis_y: int, pattern: str):
        """
        This function fill area selected  from point whit pattern in canvas board
        Parameters:
        axis_x1: point to start in axis x
        axis_y1: point to start in axis y
        """
        if axis_x > self.wide_canvas or axis_y > self.height_canvas:
            raise Exception('Point out of area canvas')
        self._fill_quarter_from_point(axis_x=axis_x, axis_y=axis_y, value_x='left', value_y='up', pattern=pattern)
        self._fill_quarter_from_point(axis_x=axis_x, axis_y=axis_y, value_x='right', value_y='up', pattern=pattern)
        self._fill_quarter_from_point(axis_x=axis_x, axis_y=axis_y, value_x='left', value_y='down', pattern=pattern)
        self._fill_quarter_from_point(axis_x=axis_x, axis_y=axis_y, value_x='right', value_y='down', pattern=pattern)
