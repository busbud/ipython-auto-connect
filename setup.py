from setuptools import setup, find_packages

VERSION = '1.0.0'

setup(
    name = 'ipython-auto-connect',
    packages = ['ipython_auto_connect'],
    version = VERSION,
    description = 'IPython extension for auto-connecting to various databases',
    author = 'Busbud Devs',
    author_email = 'devs@busbud.com',
    url = 'https://github.com/busbud/ipython-auto-connect',
    license = 'MIT',

    install_requires = [
        'sqlalchemy',
        'psycopg2',
        'bigquery-python==1.4.0',
        'oauth2client==1.2',
        'google-api-python-client==1.2'
    ],

    zip_safe = False,
    include_package_data = True,
    package_data = {'': ['LICENSE', 'README.md']},

    keywords = ['ipython', 'sql', 'bigquery'],

    download_url = 'https://github.com/busbud/ipython-auto-connect/archive/{v}.tar.gz'.format(v=VERSION)
)
