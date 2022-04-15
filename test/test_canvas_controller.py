import pytest
from pytest import mark

from canvas_controller import CanvasController


@mark.parametrize('data_test', (({'wide': 'A', 'height': 3, 'response': 'Value wide should Integer'}),
                                ({'wide': 1, 'height': 'A', 'response': 'Value height should Integer'}),
                                ({'wide': -10, 'height': 10, 'response': 'Value wide should more that 0'}),
                                ({'wide': 10, 'height': -10, 'response': 'Value height should more that 0'}),
                                )
                  )
def test_instance_canvas_controller_error(data_test):
    with pytest.raises(Exception) as error:
        CanvasController(
            wide_canvas=data_test['wide'],
            height_canvas=data_test['height'])
    assert str(error.value) == data_test['response']


@mark.parametrize('data_test', (({'wide': 20, 'height': 4,
                                 'response': '----------------------\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '----------------------\n'}),
                                ({'wide': 4, 'height': 4,
                                 'response': '------\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '------\n'}),
                                )
                  )
def test_create_canvas(data_test):
    canvas_controller = CanvasController(
        wide_canvas=data_test['wide'],
        height_canvas=data_test['height'])
    assert canvas_controller.canvas == data_test['response']


@mark.parametrize('data_test', (({'x1': 1, 'y1': 2, 'x2': 6, 'y2': 2,
                                  'response': '----------------------\n'
                                              '|                    |\n'
                                              '|xxxxxx              |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '----------------------\n'}),
                                ({'x1': 1, 'y1': 1, 'x2': 6, 'y2': 1,
                                  'response': '----------------------\n'
                                              '|xxxxxx              |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '----------------------\n'}),
                                ({'x1': 8, 'y1': 1, 'x2': 13, 'y2': 1,
                                  'response': '----------------------\n'
                                              '|       xxxxxx       |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '----------------------\n'}),
                                ({'x1': 17, 'y1': 1, 'x2': 20, 'y2': 1,
                                  'response': '----------------------\n'
                                              '|                xxxx|\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '|                    |\n'
                                              '----------------------\n'}),
                                ({'x1': 7, 'y1': 2, 'x2': 7, 'y2': 4,
                                  'response': '----------------------\n'
                                              '|                    |\n'
                                              '|      x             |\n'
                                              '|      x             |\n'
                                              '|      x             |\n'
                                              '----------------------\n'})

                                )
                  )
def test_draw_line(data_test):
    canvas_controller = CanvasController(20, 4)
    canvas_controller.draw_line(axis_x1=data_test['x1'], axis_y1=data_test['y1'], axis_x2=data_test['x2'], axis_y2=data_test['y2'])
    assert canvas_controller.canvas == data_test['response']


@mark.parametrize('data_test', (({'line_one': {'x1': 1, 'y1': 2, 'x2': 6, 'y2': 2},
                                  'line_two': {'x1': 6, 'y1': 3, 'x2': 6, 'y2': 4},
                                  'response': '----------------------\n'
                                              '|                    |\n'
                                              '|xxxxxx              |\n'
                                              '|     x              |\n'
                                              '|     x              |\n'
                                              '----------------------\n'}),
                                )
                  )
def test_draw_some_lines(data_test):
    line_one = data_test['line_one']
    line_two = data_test['line_two']
    canvas_controller = CanvasController(20, 4)
    canvas_controller.draw_line(axis_x1=line_one['x1'], axis_y1=line_one['y1'], axis_x2=line_one['x2'], axis_y2=line_one['y2'])
    canvas_controller.draw_line(axis_x1=line_two['x1'], axis_y1=line_two['y1'], axis_x2=line_two['x2'], axis_y2=line_two['y2'])
    assert canvas_controller.canvas == data_test['response']


@mark.parametrize('data_test', (({'x1': 1, 'y1': 1, 'x2': 20, 'y2': 4, 'response': 'This app not draw diagonal lines'}),
                                ({'x1': 'A', 'y1': 1, 'x2': 20, 'y2': 4, 'response': 'All values should be integers'}),
                                ({'x1': 1, 'y1': 'B', 'x2': 20, 'y2': 4, 'response': 'All values should be integers'}),
                                ({'x1': 1, 'y1': 1, 'x2': '20', 'y2': 4, 'response': 'All values should be integers'}),
                                ({'x1': 1, 'y1': 1, 'x2': 20, 'y2': '4', 'response': 'All values should be integers'}),
                                ({'x1': 30, 'y1': 1, 'x2': 35, 'y2': 4, 'response': 'Line out of area canvas'}),
                                ({'x1': 1, 'y1': 1, 'x2': 35, 'y2': 4, 'response': 'Line out of area canvas'}),
                                ({'x1': 1, 'y1': 6, 'x2': 6, 'y2': 8, 'response': 'Line out of area canvas'}),
                                ({'x1': 1, 'y1': 4, 'x2': 35, 'y2': 8, 'response': 'Line out of area canvas'}),
                                ))
def test_draw_manage_errors(data_test):
    canvas_controller = CanvasController(20, 4)
    with pytest.raises(Exception) as error:
        canvas_controller.draw_line(axis_x1=data_test['x1'], axis_y1=data_test['y1'], axis_x2=data_test['x2'], axis_y2=data_test['y2'])
    assert canvas_controller.canvas == '----------------------\n' \
                                       '|                    |\n' \
                                       '|                    |\n' \
                                       '|                    |\n' \
                                       '|                    |\n' \
                                       '----------------------\n'
    assert str(error.value) == data_test['response']


@mark.parametrize('data_test', (({'square': {'x1': 16, 'y1': 1, 'x2': 20, 'y2': 3},
                                  'response': '----------------------\n'
                                              '|               xxxxx|\n'
                                              '|               x   x|\n'
                                              '|               xxxxx|\n'
                                              '|                    |\n'
                                              '----------------------\n'}),
                                )
                  )
def test_draw_square(data_test):
    square = data_test['square']
    canvas_controller = CanvasController(20, 4)
    canvas_controller.draw_rectangle(axis_x1=square['x1'], axis_x2=square['x2'], axis_y1=square['y1'], axis_y2=square['y2'])
    assert canvas_controller.canvas == data_test['response']


def test_blank_fill():
    canvas_controller = CanvasController(20, 4)
    canvas_controller.draw_line(axis_x1=1, axis_y1=2, axis_x2=6, axis_y2=2)
    canvas_controller.draw_line(axis_x1=6, axis_y1=3, axis_x2=6, axis_y2=4)
    canvas_controller.draw_rectangle(axis_x1=16, axis_y1=1, axis_x2=20, axis_y2=3)
    canvas_controller.bucket_fill(3, 3)
    assert canvas_controller.canvas == '----------------------\n'\
                                       '|oooooooooooooooxxxxx|\n'\
                                       '|xxxxxxooooooooox   x|\n'\
                                       '|     xoooooooooxxxxx|\n'\
                                       '|     xoooooooooooooo|\n'\
                                       '----------------------\n'
