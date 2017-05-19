
from setuptools import setup, find_packages
setup(
	name='normanpd',
	version='1.0',
	author='Andrew Duffle',
	author_email='andrew.g.duffle@ou.edu',
	packages=find_packages(exclude=('test','docs'))
)

