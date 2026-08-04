from setuptools import setup, find_packages
from typing import List

def get_requires(file_path: str) -> List[str]:
    " this function will return the list of requirements "

    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets = [req.replace("\n", "") for req in requiremnets]


        return requiremnets

setup(name= 'ml project',
        version= '0.1',
        description= 'ML project',
        author= 'Rohan',
        packages= find_packages(),
        install_requires= [get_requires('requirements.txt')]
)
