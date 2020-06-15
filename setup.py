from setuptools import setup, find_packages

setup(
    name='ChatBot',
    version='1.0',
    description='ChatBot Project',
    author='minhdao',
    packages=find_packages(exclude=[
        'docs',
        'tests',
        'static',
        'templates',
        '.gitignore',
        'README.md',
        'data',
        'saved_models'
    ]),
    install_requires=[
        'pylint',
        'autopep8',
        'flask',
        'elasticsearch',
        'underthesea',
        'flask-pymongo',
        'python-dotenv',
        'tensorflow',
        'numpy',
        'scikit-learn',
    ],
)
