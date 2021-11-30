from setuptools import find_packages, setup
import versioneer

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="housing",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Guillaume Alleon",
    author_email="guillaume.alleon@gmail.com",
    description="A price house predictor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    scripts=["scripts/home-run"],
    zip_safe=False,
)
