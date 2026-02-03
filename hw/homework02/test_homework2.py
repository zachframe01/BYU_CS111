from pathlib import Path
from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import test_files, with_import, tier
from pytest import approx

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


def compare_images(obs: Path | PILImage.Image, exp: Path | PILImage.Image):
    if not isinstance(obs, PILImage.Image):
        observed = PILImage.open(obs).convert('RGB')
    else:
        observed = obs
    if not isinstance(exp, PILImage.Image):
        expected = PILImage.open(exp).convert('RGB')
    else:
        expected = exp

    assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

    diff = ImageChops.difference(observed, expected)
    if bbox := diff.getbbox():
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                if not observed_pixel or not expected_pixel:
                    assert False, f"Failed to get pixels at ({x}, {y})!"

                if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                    assert False, "Failed to get correct pixel type!"

                assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`."
                assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`."
                assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`."

    if isinstance(obs, Path):
        obs.unlink(missing_ok=True)


@core
@with_import('homework2', 'darken')
def test_CORE_darken(darken):
    observed = darken(test_files / 'cougar.png', 0.8)
    compare_images(observed.image, test_files / 'cougar_darkened.key.png')


@core
@with_import('homework2', 'grayscale')
def test_CORE_grayscale(grayscale):
    observed = grayscale(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_grayscale.key.png')


@core
@with_import('homework2', 'sepia')
def test_CORE_sepia(sepia):
    observed = sepia(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_sepia.key.png')


@advanced
@with_import('homework2', 'flipped')
def test_ADVANCED_flipped_with_landscape(flipped):
    observed = flipped(test_files / 'landscape.png')
    compare_images(observed.image, test_files / 'landscape_flipped.key.png')


@advanced
@with_import('homework2', 'flipped')
def test_ADVANCED_flipped_with_flamingo_float(flipped):
    observed = flipped(test_files / 'flamingo-float.png')
    compare_images(observed.image, test_files / 'flamingo-float_flipped.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_landscape(make_borders):
    observed = make_borders(test_files / 'landscape.png', 30, 0, 255, 0)
    compare_images(observed.image, test_files / 'landscape_border.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_flamingo_float_10(make_borders):
    observed = make_borders(test_files / 'flamingo-float.png', 10, 0, 255, 255)
    compare_images(observed.image, test_files / 'flamingo-float_border_10.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_flamingo_float_5(make_borders):
    observed = make_borders(
        test_files / 'flamingo-float.png', 5, 255, 125, 125)
    compare_images(observed.image, test_files / 'flamingo-float_border_5.key.png')
