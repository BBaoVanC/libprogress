import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libprogress",
    version="3.0.1",
    author="BBaoVanC",
    author_email="bbaovanc@protonmail.com",
    description="Library containing progress bar generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BBaoVanC/libprogress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
