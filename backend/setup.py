import os
import re
from setuptools import setup, find_packages

def get_version():
    version_file = os.path.join('src/antibody_binding_api', '_version.py')
    with open(version_file, 'r') as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

setup(
    name='antibody_analysis_fastapi',
    version=get_version(),
    description='A FastAPI backend for analyzing antibody binding data',
    author='Neeli Katti',
    author_email='ngkatti@hotmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'antibody-analysis=app.main:app',
        ],
    },
)