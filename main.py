import sys

from canvas_controller import CanvasController


class MainApp:
    """
    This is class reads input file to process data and execute order to finally write in output file
    Attributes:
        _input_file_name (str): file name with extension .txt where extract orders to exec in canvas board
        _output_file_name (str): file name where with extension .txt write all orders executed in canvas board
        _input_lines (list): list where save lines to execute orders in canvas board
        _output_lines (list) list where save lines to write in output file after executed all order in canvas board

    Returns:
        Create a file with name _output_file_name

    Example:
        app = MainApp(input_file_name='input.txt', output_file_name='output.txt')
        app.execute_file()

    """

    def __init__(self, input_file_name: str, output_file_name: str):
        """
                The constructor for MainApp class.

                Parameters:
                    input_file_name (str): file name with extension .txt where extract orders to
                    execute in canvas board
                    output_file_name (str): file name where with extension .txt write all orders
                    executed in canvas board
                """
        self._input_file_name = input_file_name
        self._output_file_name = output_file_name
        self._input_lines = None
        self._output_lines = None
        self._read_file()

    def _read_file(self):
        with open(self._input_file_name, 'r') as file:
            self._input_lines = file.readlines()

    def _write_file(self):
        with open(self._output_file_name, 'w') as file:
            file.writelines(self._output_lines)

    def execute_file(self):
        """
                The function execute all order in _input_lines and write _output_lines after execute all
                order in canvas board.

                Returns:
                    Create a file with name _output_file_name
         """
        line = self._input_lines[0].split()
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
    MainApp(sys.argv[1], sys.argv[2]).execute_file()
