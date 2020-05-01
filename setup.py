from setuptools import setup, find_packages

setup(
    name='ChatBot',
    version='1.0',
    description='ChatBot Project',
    author='minhdao',
    packages=find_packages(exclude=[
        'tests', 'static', 'templates', '.gitignore', 'README.md'
    ]),
    install_requires=[
        'flask', 'pymongo', 'elasticsearch', 'underthesea'
    ],
)
