from setuptools import setup, find_packages





setup(
    name= "catboost",
    version = "0.0.1",
    author = "Ayush",
    author_email = "singh.ayushk1128@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)