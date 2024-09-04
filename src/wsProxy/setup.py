from setuptools import setup, find_packages

setup(
    name='wsProxy',
    version='1.0.0',
    author='Mobilis In Mobili',
    author_email='vgeekv@163.com',
    description='websocket proxy for web3 signer',
    packages=find_packages(),
    install_requires=[
        'websockets',
        'web3'
    ],
)