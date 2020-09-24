import pathlib

from setuptools import find_packages, setup

import versioneer

LONG_DESCRIPTION = """
Ibis_dask is a dask plugin for Ibis.

Ibis is a productivity-centric Python big data framework.
See http://ibis-project.org for more information.

Dask is a flexible parallel computing library for analytics.
See https://dask.org/ for more information.
"""

install_requires = [
    line.strip()
    for line in pathlib.Path(__file__)
    .parent.joinpath('requirements.in')
    .read_text()
    .splitlines()
]

dev_requires = install_requires + [
    line.strip()
    for line in pathlib.Path(__file__)
    .parent.joinpath('requirements_dev.in')
    .read_text()
    .splitlines()
    if line != "-r requirements.in"
]

setup(
    name='ibis_dask',
    url='https://github.com/ibis-project/ibis-dask',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=install_requires,
    python_requires='>=3.7',
    entry_points={
        'ibis.backends': 'dask=ibis_dask'
    },
    extras_require={
        'develop': dev_requires,
    },
    description="Dask backend for Ibis",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    license='Apache License, Version 2.0',
)
