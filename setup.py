from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = 'e .'
def get_requirements(file_path:str)->List[str]:
    """This function returns a list of requirements"""
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines() #readlines will read all the packages but it will add new line
        #character hence we will have to remove it as well
        requirements = [x.replace('\n','') for x in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

        
setup(
name  = 'mlproject',
version= '0.0.1',
author='shivdatta',
author_email='shivdatta@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt'),
)


