from setuptools import setup, find_packages

setup(
    name='pybincompiler',
    version='0.0.2',
    description='Compiler for binary code to be compiled into Python',
    author='jiwonyu',
    author_email='waterflame0221@gmail.com',
    url='https://github.com/JohnYuPromptwSpace/PyBinCompiler',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['jiwonyu', 'waterflame0221', 'python', 'binary', 'compiler'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)