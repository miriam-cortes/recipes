from setuptools import setup, find_packages

setup(
    name='recipes_api',
    version='0.1.0',
    url='https://github.com/miriam-cortes/recipes',
    author='Miriam Cortes',
    packages=find_packages(),
    install_requires=[
        'flask-restx==0.2',
        'Flask-SQLAlchemy==2.4'
    ],
)
