from setuptools import setup, find_packages

hyphen_e_dot = '-e .'
req=[]

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()
    if hyphen_e_dot in read_requirements():
        read_requirements().remove(hyphen_e_dot)
    return read_requirements()

setup=setup(
    name='V1_App',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ],
    description='A sample Python application',
    author='Prathamesh More',
    author_email='prathamesh162002@gmail.com',
    url="https://github.com/pratha16/ML_project/tree/main"
)