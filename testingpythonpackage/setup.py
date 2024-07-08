from setuptools import setup, find_packages

setup(
    name="testing_python_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    description="A simple example package",
    author="Carlos Augusto",
    author_email="capv2004@gmail.com",
    url="https://github.com/CarlosAugustoP/python-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
