"""このファイルはinit.pyに含まれていない."""

import poetry_stabs_package_sample
import poetry_stabs_package_sample.types
import poetry_stabs_package_sample.types.commonmodels
import poetry_stabs_package_sample.types.sampleTypes


def my_feel(i: int = 3) -> poetry_stabs_package_sample.types.sampleTypes.Emotion:
    """My feeling."""
    return poetry_stabs_package_sample.types.sampleTypes.Emotion(i)
