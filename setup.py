from setuptools import setup, find_packages

setup(
    name="quantum-ai-accelerator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    author="Yann LeCun",
    description="Hybrid quantum-classical optimization framework for next-gen AI workloads.",
    url="https://github.com/YannLeCun25/quantum-ai-accelerator",
)
