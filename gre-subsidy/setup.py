from distutils.core import setup
from distutils.extension import Extension

setup(name="gre_subsidy",
    ext_modules=[
        Extension("gre_subsidy", ["gre_GetBlockBaseValue.cpp"],
        libraries = ["boost_python"])
    ])
