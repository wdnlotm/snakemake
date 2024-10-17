__author__ = "Myles Kim"
__copyright__ = "Copyright 2024, Myles Kim"
__email__ = "mkim@mkim.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell


shell(
    "echo $PWD > {snakemake.output}")
