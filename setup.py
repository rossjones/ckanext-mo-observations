from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-mo-observations',
	version=version,
	description="Retrieves observation data from the Met Office",
	long_description="""\
	""",
	classifiers=[],
	keywords='',
	author='Ross Jones',
	author_email='ross@servercode.co.uk',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.mo_observations'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'requests==0.14',
	],
	entry_points=\
	"""
        [paste.paster_command]
        update = ckanext.mo_observations.command:UpdateData
	""",
)
