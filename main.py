import sys

from canvas_controller import CanvasController


class MainApp:
    def __init__(self):
        self._input_lines = None
        self._output_lines = None

    def _read_file(self):
        with open(sys.argv[1], 'r') as file:
            self._input_lines = file.readlines()

    def _write_file(self):
        with open(sys.argv[2], 'w') as file:
            file.writelines(self._output_lines)

    def execute_file(self):
        self._read_file()
        line = self._input_lines[0].split()
        print(line)
        if line[0] != 'C':
            raise Exception('Is need first create Canvas board, The first line should be (C {value_x} {value_y})')
        canvas_controller = CanvasController(int(line[1]), int(line[2]))
        print(canvas_controller.canvas)
        actions = {
            'C': canvas_controller,
            'L': canvas_controller.draw_line,
            'R': canvas_controller.draw_rectangle,
            'B': canvas_controller.bucket_fill
        }
        self._output_lines = [canvas_controller.canvas]
        for line in self._input_lines:
            if not line[0] == 'C':
                params = []
                line = line.split()
                action = line.pop(0)
                for param in line:
                    if param.isnumeric():
                        params.append(int(param))
                    else:
                        params.append(param)
                actions[action](*params)
                self._output_lines.append(canvas_controller.canvas)
                print(canvas_controller.canvas)
            self._write_file()


if __name__ == '__main__':
    MainApp().execute_file()
