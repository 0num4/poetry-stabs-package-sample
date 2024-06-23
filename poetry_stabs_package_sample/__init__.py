# https://github.com/psf/requests/blob/main/src/requests/__init__.py#L143
# requestsは相対インポート使ってるな
from . import sample, sample2

__all__ = ["sample", "sample2"]
