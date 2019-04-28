import setuptools
from piat import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piat",
    version=__version__,
    author=__author__,
    author_email="aaqrabaw@gmail.com",
    description="Syslog and Trap service API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ali-aqrabawi/piat",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pysnmp'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
