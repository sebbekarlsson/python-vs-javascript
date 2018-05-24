from setuptools import setup


setup(
    name='jsonapi',
    version='1.0',
    install_requires=[
        'bcrypt',
        'flask'
    ],
    packages=[
        'jsonapi'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
