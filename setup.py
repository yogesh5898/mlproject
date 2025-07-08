from setuptools import find_packages, setup
from typing import List

HYPEN_E='-e .'
def get_requirements(filepath:str)->list[str]:
    """
    This will return list of requirements
    """
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

    if HYPEN_E in requirements:
        requirements.remove(HYPEN_E)

    return requirements

setup(
    name='mlproject',
    version='0.01',
    author='Yogesh',
    author_email='yogesh050898@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
