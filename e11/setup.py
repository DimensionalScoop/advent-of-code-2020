from setuptools import setup
from Cython.Build import cythonize
from Cython.Compiler import Options
import numpy

comp_dirs = {
    "boundscheck":False,
    "wraparound":False
    }

setup(
    name='simulation',
    ext_modules=cythonize("simulate.pyx",compiler_directives=comp_dirs),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)