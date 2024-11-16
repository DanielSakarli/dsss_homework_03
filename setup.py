from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    url="https://github.com/DanielSakarli/dsss_homework_02",
    license="Apache License 2.0",
    author="Daniel Sakarli",
    author_email="daniel-sakarli@hotmail.de",
    description="Applying unit tests to basic math operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)