import pathlib
from setuptools import setup

# reading the README file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

# the setup script
setup(
    name="skkuossp",
    version="1.0.0",
    description="The SKKU OSSP Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="empty",
    author="<your name>",
    author_email="<your email adderss>",
    license="MIT",
    packages=["skkuossp"], # this is important!    
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
   
)