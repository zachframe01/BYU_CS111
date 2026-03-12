from byu_pytest_utils import with_import
import ast
import inspect


@with_import('tree_recursion', 'echo_twice')
def test_Q1_echo_twice(echo_twice, capfd):
    echo_twice('hello', 2)
    out, _ = capfd.readouterr()
    assert out == "helloAA\nhelloAB\nhelloBA\nhelloBB\n"

    echo_twice('cat', 0)
    out, _ = capfd.readouterr()
    assert out == "cat\n"

    echo_twice('e', 4)
    out, _ = capfd.readouterr()
    assert out == "eAAAA\neAAAB\neAABA\neAABB\neABAA\neABAB\neABBA\neABBB\neBAAA\neBAAB\neBABA\neBABB\neBBAA\neBBAB\neBBBA\neBBBB\n"


@with_import('tree_recursion', 'ways_to_climb')
def test_Q2_ways_to_climb(ways_to_climb):
    assert ways_to_climb(4) == 5
    assert ways_to_climb(0) == 1
    assert ways_to_climb(1) == 1
    assert ways_to_climb(10) == 89


@with_import('tree_recursion', 'paths')
def test_Q3_paths(paths):
    tree = ast.parse(inspect.getsource(paths))
    recursive_call_seen = any(
        isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'paths'
        for node in ast.walk(tree)
    )

    if not recursive_call_seen:
        raise Exception('In the paths function, you must make a recursive call to the paths function')

    for m, n, expected in [(1, 1, 1), (2, 2, 2), (3, 3, 6), (5, 7, 210), (117, 1, 1), (1, 157, 1), (0, 0, 0), (0, 5, 0), (5, 0, 0)]:
        result = paths(m, n)
        assert result == expected, f"Expected {expected} paths for {m}, {n}, got {result}"


@with_import('tree_recursion', 'phone_keypad')
def test_Q4_phone_keypad(phone_keypad, capfd):
    phone_keypad('23')
    out, _ = capfd.readouterr()
    assert out == "AD\nAE\nAF\nBD\nBE\nBF\nCD\nCE\nCF\n"

    phone_keypad('159')
    out, _ = capfd.readouterr()
    assert out == "1JW\n1JX\n1JY\n1JZ\n1KW\n1KX\n1KY\n1KZ\n1LW\n1LX\n1LY\n1LZ\n"

    phone_keypad('8')
    out, _ = capfd.readouterr()
    assert out == "T\nU\nV\n"
