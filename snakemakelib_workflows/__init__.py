# Copyright (c) 2013 Per Unneberg
import os

__import__('pkg_resources').declare_namespace(__name__)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

SNAKEMAKELIB_WORKFLOWS_PATH = os.path.dirname(__file__)

