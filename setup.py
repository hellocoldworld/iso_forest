import sys
import os
from distutils.core import setup
prjdir = os.path.dirname(__file__)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

extra_link_args = []
libraries = []
library_dirs = []
include_dirs = []
__version__ = '1.0.0'
#exec(open('easyaccess/version.py').read())
setup(
    name='isoforest',
    version=__version__,
    author='Matias Carrasco Kind',
    author_email='mcarras2@illinois.edu',
    scripts=[],
    py_modules=['iso'],
    packages=[],
    license='License.txt',
    description='Isolation Forest for anomalous detection',
    long_description=read('README.md'),
    url='https://github.com/mgckind/iso_forest',
    install_requires=[],
)