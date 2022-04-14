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
        canvas_controller = CanvasController(data_test['wide'], data_test['height'])
    assert str(error.value) == data_test['response']


@mark.parametrize('data_test', (({'wide': 20, 'height': 4,
                                 'response': '----------------------\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '|                    |\n'
                                             '----------------------'}),
                                ({'wide': 4, 'height': 4,
                                 'response': '------\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '|    |\n'
                                             '------'}),
                                )
                  )
def test_create_canvas(data_test):
    canvas_controller = CanvasController(data_test['wide'], data_test['height'])
    assert canvas_controller.canvas == data_test['response']
