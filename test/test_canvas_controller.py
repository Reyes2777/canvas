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
                                              '----------------------\n'})

                                )
                  )
def test_draw_line(data_test):
    canvas_controller = CanvasController(20, 4)
    canvas_controller.draw_line(x1=data_test['x1'], y1=data_test['y1'], x2=data_test['x2'], y2=data_test['y2'])
    assert canvas_controller.canvas == data_test['response']

