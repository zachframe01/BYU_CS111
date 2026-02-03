from byu_pytest_utils import dialog, test_files, this_folder, ensure_missing, visibility, tier
import ast


core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


def create_doubled_constants_file(source_file, output_file):
    """Reads the source file, doubles all constants, and saves the result to output_file."""
    with open(source_file, "r") as src:
        lines = src.readlines()

    with open(output_file, "w") as dest:
        for line in lines:
            if '=' not in line:
                dest.write(line)
                continue

            var, val = line.split("=", 1)
            var, val = var.split(':')[0].strip(), val.strip()
            if var == "PI" or not var.isidentifier() or not var.isupper():
                dest.write(line)
                continue

            try:
                value = ast.literal_eval(val)
                if isinstance(value, (int, float, complex)):
                    doubled_value = value * 2
                    dest.write(f"{var} = {doubled_value}\n")
                else:
                    dest.write(line)
            except:
                dest.write(line)

    return output_file


@core
@dialog(test_files / "test_CORE_1_person.txt", this_folder / "homework0.py")
def test_CORE_1_person():
    ...


@core
@dialog(test_files / "test_CORE_3_person.txt", this_folder / "homework0.py")
def test_CORE_3_person():
    ...


@core
@dialog(test_files / "test_CORE_4_person.txt", this_folder / "homework0.py")
def test_CORE_4_person():
    ...


@core
@dialog(test_files / "test_CORE_7_person.txt", this_folder / "homework0.py")
def test_CORE_7_person():
    ...


@core
@dialog(test_files / "test_CORE_8_person.txt", this_folder / "homework0.py")
def test_CORE_8_person():
    ...


@core
@dialog(test_files / "test_CORE_10_person.txt", this_folder / "homework0.py")
def test_CORE_10_person():
    ...


@core
@dialog(test_files / "test_CORE_11_person.txt", this_folder / "homework0.py")
def test_CORE_11_person():
    ...


@core
@dialog(test_files / "test_CORE_12_person.txt", this_folder / "homework0.py")
def test_CORE_12_person():
    ...


@core
@dialog(test_files / "test_CORE_13_person.txt", this_folder / "homework0.py")
def test_CORE_13_person():
    ...


@core
@dialog(test_files / "test_CORE_14_person.txt", this_folder / "homework0.py")
def test_CORE_14_person():
    ...


@core
def test_CORE_code_works_after_double_transformation():
    new_file_name = this_folder / "homework0-doubled-syntax-test.py"
    create_doubled_constants_file(this_folder / "homework0.py", this_folder / new_file_name)
    try:
        ast.parse(open(this_folder / new_file_name).read())
        assert  True, "Successfully parsed a file with doubled constants."
        new_file_name.unlink(missing_ok=True)
    except SyntaxError as e:
        new_file_name.unlink(missing_ok=True)
        assert False, f"New '{new_file_name}' file with doubled constants has a syntax error: {e}\n\nPlease check you only uppercase the constants and have them in the global space (not inside the method).\nOther variables should be lowercase."


@core
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_CORE_15_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_CORE_15_person_doubled():
    ...


@core
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_CORE_16_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_CORE_16_person_doubled():
    ...


@core
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_CORE_17_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_CORE_17_person_doubled():
    ...


@core
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_CORE_100_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_CORE_100_person_doubled():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_1_person.txt", this_folder / "homework0.py")
def test_ADVANCED_1_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_3_person.txt", this_folder / "homework0.py")
def test_ADVANCED_3_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_4_person.txt", this_folder / "homework0.py")
def test_ADVANCED_4_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_7_person.txt", this_folder / "homework0.py")
def test_ADVANCED_7_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_8_person.txt", this_folder / "homework0.py")
def test_ADVANCED_8_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_10_person.txt", this_folder / "homework0.py")
def test_ADVANCED_10_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_11_person.txt", this_folder / "homework0.py")
def test_ADVANCED_11_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_12_person.txt", this_folder / "homework0.py")
def test_ADVANCED_12_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_13_person.txt", this_folder / "homework0.py")
def test_ADVANCED_13_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_14_person.txt", this_folder / "homework0.py")
def test_ADVANCED_14_person():
    ...


@advanced
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_ADVANCED_15_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_ADVANCED_15_person_doubled():
    ...


@advanced
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_ADVANCED_16_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_ADVANCED_16_person_doubled():
    ...


@advanced
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_ADVANCED_17_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_ADVANCED_17_person_doubled():
    ...


@advanced
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_ADVANCED_100_person.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_ADVANCED_100_person_doubled():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_1_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_1_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_3_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_3_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_4_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_4_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_7_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_7_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_8_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_8_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_10_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_10_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_11_person_10_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_11_person_10_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_12_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_12_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_13_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_13_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_14_person_10_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_14_person_10_tip():
    ...


@excellent
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_EXCELLENT_15_person_35_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_EXCELLENT_15_person_35_tip_doubled():
    ...


@excellent
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_EXCELLENT_16_person_80_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_EXCELLENT_16_person_80_tip_doubled():
    ...


@excellent
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_EXCELLENT_17_person_10_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_EXCELLENT_17_person_10_tip_doubled():
    ...


@excellent
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_EXCELLENT_100_person_80_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_EXCELLENT_100_person_80_tip_doubled():
    ...


@core
@ensure_missing(this_folder / 'homework0-doubled.py')
@visibility('hidden')
def test_doubled_clean():
    ...
