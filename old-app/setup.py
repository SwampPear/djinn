from setuptools import setup, find_packages

setup(
    name='djinn',
    version='0.1',
    packages=find_packages(where='djinn'),
    package_dir={'': 'djinn'},
    entry_points={
        'console_scripts': [
            'djinn = djinn:main'
        ]
    },
    install_requires=[]
)