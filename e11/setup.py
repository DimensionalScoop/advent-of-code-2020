from setuptools import setup
from Cython.Build import cythonize
from Cython.Compiler import Options
import numpy

setup(
    name='simulation',
    ext_modules=cythonize("simulate.pyx", gdb_debug=False),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)