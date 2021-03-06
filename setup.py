import sys
from setuptools import setup, find_packages

requires = [
    'requests>=2.18.4',
    'tqdm>=3.8.0'
]

    requires.append('configparser')

setup(
    name="image-scraper",
    version="0.0.1",
    description=("command line application for image scraping on instagram written in python"),
    url="https://github.com/maddarauci/image-scraper",
    author="MadDom",
    packages=find_packages(exclude=["tests"]),
    install_requirements=requires,
    entry_point={
        console_scripts: ['image-scraper=image-scraper.app:main']
     },
    tests_suite="noise.collector",
    zip_safe=False,
    keywords=['instagram', 'scraper', 'download', 'image']

)

