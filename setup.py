from setuptools import setup, find_packages

setup(
    name="local_llm",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ollama",
        "requests",
    ],
    python_requires=">=3.8",
    author="cypheroxide",
    description="A Local LLM toolkit for autonomous AI operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
