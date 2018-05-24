from setuptools import setup, find_packages


setup(
    name='jsonapi',
    version='1.0',
    install_requires=[
        'bcrypt',
        'flask'
    ],
    packages=find_packages(exclude=[
        "*.tests",
        "*.tests.*",
        "tests.*",
        "tests",
        "*tests*",
        "*.pyc"
    ]),
    data_files=[('', ['__main__.py', ])],
    entry_points={
        'console_scripts': [
        ]
    }
)
