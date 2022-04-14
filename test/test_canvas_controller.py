from pytest import mark

from canvas_controller import CanvasController


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



