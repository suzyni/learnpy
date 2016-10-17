try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Suzy',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'nsr17@126.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['people'],
    'scripts': ['bin/title.py'],
    'name': 'project1'
}

setup(**config)
