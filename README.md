README
======

This Project Canvas is challenge proposed by Huge.

How use app
-------

Write file with extension .txt whit next params:

* Use C to create canvas
* Use L to create line
* Use R to create rectangle
* Use F to create fill

Example  input file:

    C 20 4
    L 1 2 6 2
    L 6 3 6 4
    R 16 1 20 3
    B 10 3 o

Execute next command ``python3 main.py input.txt output.txt`` response new file ouput.txt in branch with the next cointain:

        ----------------------
        |                    |
        |                    |
        |                    |
        |                    |
        ----------------------
        ----------------------
        |                    |
        |xxxxxx              |
        |                    |
        |                    |
        ----------------------
        ----------------------
        |                    |
        |xxxxxx              |
        |     x              |
        |     x              |
        ----------------------
        ----------------------
        |               xxxxx|
        |xxxxxx         x   x|
        |     x         xxxxx|
        |     x              |
        ----------------------
        ----------------------
        |oooooooooooooooxxxxx|
        |xxxxxxooooooooox   x|
        |     xoooooooooxxxxx|
        |     xoooooooooooooo|
        ----------------------


Testing
-------

Run all tests with ``pytest -s -vvvv``. For more uses of pytest, `check this <https://docs.pytest.org/en/latest/usage.html>`_.