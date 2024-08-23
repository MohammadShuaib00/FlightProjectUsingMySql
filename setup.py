from setuptools import find_packages, setup

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='flight',
    version='0.0.1',
    author='Mohammad Shuaib',
    author_email='mohammadshuaib3455@gmail.com',
    description='A package for flight-related operations',
    packages=find_packages(),
    install_requires=install_requires,  # Automatically fetch dependencies from requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
