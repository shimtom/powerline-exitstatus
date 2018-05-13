# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name         = 'powerline-exitstatus',
    description  = 'A Powerline segment for showing the status of Exit status',
    version      = '1.0.0',
    keywords     = 'powerline exit status prompt',
    license      = 'MIT',
    author       = 'shimtom',
    author_email = 'shimtom1230@gmail.com',
    url          = 'https://github.com/shimtom/powerline-exitstatus',
    packages     = ['powerline_exitstatus'],
    install_requires = ['powerline-status'],
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)