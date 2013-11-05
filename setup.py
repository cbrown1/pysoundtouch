#!/usr/bin/env python
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
#from Cython.Build import cythonize
import numpy

ext_modules = [ 
        Extension(
            name = "soundtouch",
            sources = ["src/st.pyx", "src/shiftpitch.cpp"],
            include_dirs = [ numpy.get_include(), "/usr/include/soundtouch", "/usr/local/include/soundtouch", "soundtouch-1.7.1\soundtouch\include"],
            libraries = ["SoundTouch"],
            library_dirs = ["soundtouch-1.7.1\soundtouch\lib"],
            language = "c++",
            )
        ]

setup(name='soundtouch',
    version = "0.1",
    description='A python wrapper to the soundtouch pitch shift algorithm',
    long_description='''\
    A wrapper to soundtouch, an algorithm for pitch shifting
    based pitch algorith.''',
    author='Christopher Brown',
    author_email='cbrown1@pitt.edu',
    maintainer='Christopher Brown',
    maintainer_email='cbrown1@pitt.edu',
    url='http://pysoundtouch.googlecode.com',
    cmdclass = {'build_ext':build_ext},
    ext_modules = ext_modules
)
