from re import search

from setuptools import setup

with open('src/cuborg/__init__.py') as f:
    version = str(search(r"__version__ = '(.*)'", f.read()).group(1))

with open('README.md') as f:
    long_description = f.read()

setup(
    name='cuborg',
    version=version,
    packages=[
        'cuborg',
    ],
    package_dir={'': 'src'},
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    url='https://github.com/mon4ter/cuborg',
    license='MIT',
    author='Dmitry Galkin',
    author_email='mon4ter@gmail.com',
    description='Space efficient backups for your Minecraft server using Borg',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
