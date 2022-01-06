from setuptools import find_packages, setup

base_dependencies = [
    "pandas>=1.0.0",
    "python-dateutil>=2",
]


additional_dependencies = {
    "dev": ["black>=21.9b0", "pre-commit>=2.15.0", "pytest>=6.2.1", "pylint>=2.7.4", "jupyterlab"],
}


setup(
    name="rutil",
    packages=find_packages(where="rutil"),
    package_dir={"": "rutil"},
    description=("A srt translation from R to Python"),
    author="Ismael Cabral",
    version="0.0.1",
    py_modules=["rutil"],
    install_requires=base_dependencies,
    extras_require=additional_dependencies,
)


