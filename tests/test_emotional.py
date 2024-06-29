"""Test the no_include__init__py.py."""

from poetry_stabs_package_sample import no_include__init__py
import poetry_stabs_package_sample
import poetry_stabs_package_sample.types
import poetry_stabs_package_sample.types.sampleTypes


def test_my_feel():
    """Test the my_feel function."""
    assert no_include__init__py.my_feel(
        1
    ) == poetry_stabs_package_sample.types.sampleTypes.Emotion(1)
