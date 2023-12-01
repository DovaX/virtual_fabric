import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='virtual_fabric',
    version='0.1.0',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='High level library used for smooth orchestration of virtual machines using fabric',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/virtual_fabric',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'fabric'
     ],
    python_requires='>=3.6',
)
    