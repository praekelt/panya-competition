from setuptools import setup, find_packages

setup(
    name='django-competition',
    version='dev',
    description='Django competition app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-competition',
    packages = find_packages(),
    include_package_data=True,
)

