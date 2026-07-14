python
from setuptools import setup, find_packages

setup(
    name="brent-oil-analysis",
    version="1.0.0",
    description="Bayesian Change Point Analysis of Brent Oil Prices",
    author="[Your Name]",
    packages=find_packages(),
    install_requires=[
        "pymc>=5.0.0",
        "arviz>=0.14.0",
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "statsmodels>=0.13.0",
        "ruptures>=1.1.0",
    ],
    python_requires=">=3.8",
)
