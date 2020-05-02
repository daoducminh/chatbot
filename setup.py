from setuptools import setup, find_packages

setup(
    name='ChatBot',
    version='1.0',
    description='ChatBot Project',
    author='minhdao',
    packages=find_packages(exclude=[
        'docs', 'tests', 'static', 'templates', '.gitignore', 'README.md'
    ]),
    install_requires=[
        'flask', 'elasticsearch', 'underthesea', 'flask-pymongo', 'python-dotenv', 'pylint', 'autopep8'
    ],
)
