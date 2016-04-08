from setuptools import setup, find_packages

setup(
    name='python_connection_loader',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',
    packages = ['pythonconnectionloader'],

    description='Setup database and bigquery connections automatically in IPython',

    # The project's main homepage.
    url='',

    # Author details
    author='Busbud Devs',
    author_email='devs@busbud.com',

    # Choose your license
    license='MIT',

    # What does your project relate to?
    keywords='ipython sql bigquery',

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'sqlalchemy',
        'psycopg2',
        'bigquery-python==1.4.0',
        'oauth2client==1.2',
        'google-api-python-client==1.2'
    ],
)