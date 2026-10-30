[![Documentation](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/build_docs.yml/badge.svg)](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/build_docs.yml) 
[![Testing](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/testing.yml/badge.svg)](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/testing.yml)
[![Publishing to PyPI](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/pypi_publish.yml/badge.svg?branch=main)](https://github.com/TheoChem-VU/PyOrbb/actions/workflows/pypi_publish.yml)

# PyOrbb
Our group aims to empower chemists with state-of-the-art quantum-chemical analysis tools. The latest project is PyOrbb, used for the automated analysis of complex molecular orbital interactions. PyOrbb makes expert orbital analysis available to all chemists, regardless of their theoretical background, ensuring that knowledge knows no bounds!

Read the main article at [doi.org/10.1002/jcc.70512](https://onlinelibrary.wiley.com/doi/10.1002/jcc.70512).

## Supported Programs
PyOrbb is designed to be used with fragment calculations from the Amsterdam Density Functional (ADF) program.

## Motivation
PyOrbb assist in advanced orbital analysis for computational chemistry results from ADF. PyOrbb will generate important orbital interaction diagrams and 3D orbital visualization automatically, as well as summarise important information such as mixing coefficients, orbital populations, orbital energies and more. These properties are commonly used in computational chemical research analyses.

People often run into the following challenges:
- It may be hard to obtain a clear overview of relevant orbital interactions and .
- Data acquisition is often done manually, which can be a chaotic and laborious task.
- The information overload in the output of quantum chemical programs can be intimidating.

The aim of the PyOrbb project is:
- Enhance access to advanced orbital analyses
- To provide an efficient way to isolate all the relevant data
- Create a clear graphical representation  of the relevant data that is relevant 

Previously, our group has published the [PyFrag 2019](https://onlinelibrary.wiley.com/doi/10.1002/jcc.25871) program for the automation of fragment approaches and their quantitative analyses along a reaction coordinate. This allowed users to perform the Activation Strain Model (AMS) and the canonical energy decomposition analysis (EDA) for a whole reaction profile with one single input.

## Installation

### Installers
The latest installers can be found [here](https://github.com/TheoCheM-VU/PyOrbb/releases/latest).

### pip
Install PyOrbb via pip:
```
pip install pyorbb
```

Then start the program by running the `pyorbb` command in the command-line.

### Manual installation
The following is for people who would like to install the repository themselves. For example, to edit and/or contribute code to the project.

Clone this repository:
```
git clone git@github.com:TheoChem-VU/PyOrbb.git
```

Then move into the new directory and install the package:

```
cd PyOrbb
python -m pip install --upgrade build pip 
python -m build 
python -m pip install -e .
```

To get new updates, run:
```
git pull
```

## Contact us
If you want to report a problem or suggest an enhancement we encourage you to open an issue in this GitHub repository. Otherwise you can reach us by email (<https://www.theochem.eu/contact>).


## How to cite
If you used PyOrbb in your work you can cite it as follows:

Y. Hordijk, S. E. Beutick, X. Sun, L. Groot, T. Gijzen, J. Poater, T. A. Hamlin, F. M. Bickelhaupt, and C. Fonseca Guerra, PyOrbb—Automated Analyses of Orbital-Interaction Mechanisms, *J. Comput. Chem.* **2026**, *47*, e70512

and

Y. Hordijk, S. E. Beutick, X. Sun, L. Groot, T. Gijzen, J. Poater, T. A. Hamlin, F. M. Bickelhaupt, and C. Fonseca Guerra, PyOrbb 2026, Vrije Universiteit Amsterdam, The Netherlands


## Find out more
You Might be interested in:
- The [TheoCheM group](https://www.theochem.eu/)
- The [Vrije Universiteit Amsterdam](https://vu.nl/en)
- The [PyFrag 2019](https://github.com/TheoCheM-VU/PyFrag) program 
- Our computational chemistry automation library [TCMU](https://github.com/TheoCheM-VU/TCMU)
- For a thorough overview of the theoretical background of fragment analyses we recommend the following articles:
    - P. Vermeeren, S.C.C. van der Lubbe, C. Fonseca Guerra, F.M. Bickelhaupt, T.A.
Hamlin, _Nature Protoc._ **2020**, _15_, 649-667. (<https://doi.org/10.1038/s41596-019-0265-0>)
    - T. A. Hamlin, P. Vermeeren, C. Fonseca Guerra, F. M. Bickelhaupt.
In: _Complementary Bonding Analyses_; S. Grabowski, Ed.; De Gruyter: Berlin,
2021, pp 199-212. (<https://doi.org/10.1515/9783110660074-008>)
