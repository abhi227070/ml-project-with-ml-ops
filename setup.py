from setuptools import setup, find_packages
from typing import List

def get_packages(file_path: str) -> List[str]:
    '''
    This package takes file path and returns the list of package names in string format.
    '''
    
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
    return requirements

setup(
    name="ML Project with ML Ops",
    author="Abhijeet Maharana",
    version= "0.0.1",
    author_email= "abhijeetmaharana77@gmail.com",
    packages=find_packages(),
    install_requires = get_packages('requirements.txt')
)