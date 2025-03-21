from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pybincompiler',
    version='0.0.5',
    description='Compiler for binary code to Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='jiwonyu',
    author_email='waterflame0221@gmail.com',
    url='https://github.com/JohnYuPromptwSpace/PyBinCompiler',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pybincompiler=pybincompiler.__main__:main',
        ],
    },
)
