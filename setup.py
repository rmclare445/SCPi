from setuptools import setup

setup(
    name="SCPi",
    version="0.1",
    author="Ryan Clare",
    author_email="rmclare445@gmail.com",
    description="Sends files over scp to another local device.",
    install_requires=['paramiko','scp'],
    url="...",
    packages=['SCPi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)