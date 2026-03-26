from collections import deque
from byu_pytest_utils import this_folder, test_files, run_python_script, dialog, tier
from inspect import getdoc
from doctest import DocTestParser, DocTestRunner
import warnings


core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)

TOKENS = frozenset('#SE ')
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def _normalized(width, height):
    return tuple(value + (value + 1) % 2 for value in (width, height))


def _load_maze(path):
    assert path.exists(), f'Generated maze file {path} was not created.'
    rows = path.read_text().splitlines()
    assert rows, 'Generated maze file was empty.'
    return rows


def _walkable_region(rows, origin):
    seen = {origin}
    queue = deque([origin])
    while queue:
        x, y = queue.popleft()
        for dx, dy in STEPS:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in seen:
                continue
            if 0 <= ny < len(rows) and 0 <= nx < len(rows[ny]) and rows[ny][nx] in 'SE ':
                seen.add((nx, ny))
                queue.append((nx, ny))
    return seen


def _audit_generated_maze(path, width, height):
    rows = _load_maze(path)
    expect_w, expect_h = _normalized(width, height)

    points = {'S': [], 'E': []}
    bad = []
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char not in TOKENS:
                bad.append((x, y, char))
            elif char in points:
                points[char].append((x, y))

    border = rows[0] + rows[-1] + ''.join(row[0] + row[-1] for row in rows[1:-1])
    checklist = (
        len(rows) == expect_h,
        all(len(row) == expect_w for row in rows),
        not bad,
        points['S'] == [(1, 1)],
        points['E'] == [(expect_w - 2, expect_h - 2)],
        set(border) == {'#'},
        points['E'][0] in _walkable_region(rows, points['S'][0]),
    )
    assert all(checklist), 'Generated maze failed structural validation.'


def run_generated_maze(width, height, tmp_path, capsys):
    maze_file = tmp_path / f'generated_{width}x{height}.txt'
    run_python_script(this_folder / 'maze_solver.py', '-g', str(width), str(height), maze_file)
    captured = capsys.readouterr()
    assert 'error' not in captured.out.lower()
    _audit_generated_maze(maze_file, width, height)


@core
def test_CORE_generate_maze_3(tmp_path, capsys):
    run_generated_maze(15, 15, tmp_path, capsys)


@core
def test_CORE_generate_maze_4(tmp_path, capsys):
    run_generated_maze(50, 50, tmp_path, capsys)


@core
def test_CORE_generate_maze_5(tmp_path, capsys):
    run_generated_maze(39, 27, tmp_path, capsys)


@core
@dialog(test_files / 'maze0.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze0.txt')
def test_CORE_solve_maze_0():
    ...


@core
@dialog(test_files / 'maze2.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze2.txt')
def test_CORE_solve_maze_2():
    ...


@core
@dialog(test_files / 'maze5.solved.key.txt', this_folder / 'maze_solver.py', '-s', test_files / 'maze5.generated.key.txt')
def test_CORE_solve_maze_5():
    ...


@advanced
def test_ADVANCED_arguments_usage(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-g')
    captured = capsys.readouterr()
    assert 'usage:' in captured.out.lower()
    assert '-s' in captured.out.lower()
    assert '-g' in captured.out.lower()


@advanced
def test_ADVANCED_invalid_maze_size(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-g', '3', '3', test_files / 'maze.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert '3x5' in captured.out.lower()


@advanced
def test_ADVANCED_no_solution(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-s', test_files / 'maze1.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert 'no solution' in captured.out.lower()


@excellent
def test_EXCELLENT_generic_errors(capsys):
    run_python_script(this_folder / 'maze_solver.py', '-s', test_files / 'big_maze.txt')
    captured = capsys.readouterr()
    assert 'error' in captured.out.lower()
    assert 'maximum recursion depth exceeded' in captured.out.lower()


def class_docstring_doctest_test(cls):
    owner = getattr(cls, '__module__', None) or getattr(cls, '__name__', None)
    class_scope = {
        cls.__name__: cls,
        **{
            name: getattr(cls, name)
            for name in dir(cls)
            if callable(getattr(cls, name))
            and getattr(getattr(cls, name), '__module__', None) == owner
            and not name.startswith('__')
            and name != 'main'
        },
    }
    for func in dir(cls):
        attr = getattr(cls, func)
        if callable(attr) and getattr(attr, '__module__', None) == owner:
            if func.startswith('__') or func == 'main':
                continue
            doc = getdoc(getattr(cls, func))
            assert doc is not None, f"{func}() is missing a docstring"
            tests = DocTestParser().get_doctest(doc, class_scope, func, None, None)
            if len(tests.examples) == 0:
                warnings.warn(f"{func}() is missing doctest examples, make sure that if applicable you add them to the docstring."
                              + " Note that if you can't think of a way to write a doctest for a function, it's probably fine"
                              + " to leave it alone. This is especially true for functions that involve file operations. See the"
                              + " Code Quality Guidelines or ask your TA for more information.", UserWarning)
                continue
            runner = DocTestRunner()
            runner.run(tests)
            results = runner.summarize()
            assert results.failed == 0, f"{func}() has {results.failed} failing doctest examples"


@excellent
def test_EXCELLENT_maze_solver_docstrings():
    import maze_solver as maze_solver
    class_docstring_doctest_test(maze_solver)
