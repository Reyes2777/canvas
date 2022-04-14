from canvas_controller import CanvasController


def test_create_canvas():
    canvas_controller = CanvasController(20, 4)
    assert canvas_controller.canvas == '---------------------------\n' \
                                       '|                         |\n' \
                                       '|                         |\n' \
                                       '|                         |\n' \
                                       '|                         |\n' \
                                       '---------------------------'
