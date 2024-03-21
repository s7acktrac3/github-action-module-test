from setuptools import setup, find_packages

setup(
    name="github_action_module_test",
    version="0.1.0",
    packages=find_packages(),
    description="A simple module for GitHub Actions demo",
    author="s7acktrac3",
    author_email="s7acktrac3@example.com",
    url="https://github.com/s7acktrac3/github-action-module-test",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
