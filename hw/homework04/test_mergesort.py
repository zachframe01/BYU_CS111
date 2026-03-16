from byu_pytest_utils import test_files, this_folder, ensure_missing, tier, dialog
from inspect import getdoc
from doctest import DocTestParser, DocTestRunner
import warnings


advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


@advanced
@ensure_missing(this_folder / 'test1.output.txt')
@dialog(test_files / 'test1.key.txt', this_folder / 'mergesort.py',
        test_files / 'test1.input.txt', this_folder / 'test1.output.txt',
        output_file=this_folder / 'test1.output.txt')
def test_ADVANCED_mergesort_already_sorted_data():
    ...


@advanced
@ensure_missing(this_folder / 'test2.output.txt')
@dialog(test_files / 'test2.key.txt', this_folder / 'mergesort.py',
        test_files / 'test2.input.txt', this_folder / 'test2.output.txt',
        output_file=this_folder / 'test2.output.txt')
def test_ADVANCED_mergesort_reversed_data():
    ...


@advanced
@ensure_missing(this_folder / 'test3.output.txt')
@dialog(test_files / 'test3.key.txt', this_folder / 'mergesort.py',
        test_files / 'test3.input.txt', this_folder / 'test3.output.txt',
        output_file=this_folder / 'test3.output.txt')
def test_ADVANCED_mergesort_shuffled_data():
    ...


@advanced
@ensure_missing(this_folder / 'test4.output.txt')
@dialog(test_files / 'test4.key.txt', this_folder / 'mergesort.py',
        test_files / 'test4.input.txt', this_folder / 'test4.output.txt',
        output_file=this_folder / 'test4.output.txt')
def test_ADVANCED_mergesort_random_data():
    ...


def class_docstring_doctest_test(cls):
    for func in dir(cls):
        attr = getattr(cls, func)
        if callable(attr) and getattr(attr, '__module__', None) == getattr(cls, '__name__', None):
            if func.startswith('__') or func == 'main':
                continue
            doc = getdoc(getattr(cls, func))
            assert doc is not None, f"{func}() is missing a docstring"
            tests = DocTestParser().get_doctest(doc, {func: getattr(cls, func)}, func, None, None)
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
def test_EXCELLENT_mergesort_docstring():
    import mergesort
    class_docstring_doctest_test(mergesort)
