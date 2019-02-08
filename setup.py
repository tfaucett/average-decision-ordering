from setuptools import setup

setup(name='discriminant_ordering',
    version='0.3.3',
    description='Calculates the DO metric',
    url='http://github.com/tfaucett/discriminant_ordering',
    author='Taylor Faucett',
    author_email='tfaucett@uci.edu',
    copyright = 'Copyright 9c) 2017 Taylor Faucett',
    keywords = ['statistics', 'physics', 'math'],
    license='MIT',
    packages=['discriminant_ordering'],
    install_requires=['numpy'],
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Topic :: Education',
        'Topic :: Utilities'
        ],
      zip_safe=False)