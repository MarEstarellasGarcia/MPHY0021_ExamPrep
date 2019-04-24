from setuptools import setup, find_packages

setup(
    name="Alchemist",
    version="0.1",
    description='Packaging the reactions',
    author='Mar Estarellas',
    packages=find_packages(exclude=['*test']),
    install_requires=['argparse', 'pyyaml'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]})
