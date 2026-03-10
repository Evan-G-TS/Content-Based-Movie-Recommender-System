from setuptools import setup, find_packages
from typing import List



hyphendot = "-e ."
def get_requirements(file: str) -> List[str]:
    requirements = []
    with open(file) as file_obj:
        requirements= file_obj.readlines()

        requirements= [req.replace("\n","") for req in requirements]

        if hyphendot in requirements:
            requirements.remove(hyphendot)

        return requirements


setup(
    name= "Content based movie recommender system",
    author="Evan.G.Ts",
    author_email= "evan.tsiotsias@gmail.com",
    version= "0.0.1",
    install_requires= get_requirements("requirements.txt"),
    packages= find_packages()
)

