from setuptools import setup, find_packages

requires = [
    'mysqlclient',
    'SQLAlchemy',
    'flask',
    'flask-admin',
    'flask-sqlalchemy'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-xdist',
    'pytest-codestyle',
]

setup(
    name='flask-poc',
    version='0.0.1',
    description='Flask Admin proof of concept',
    long_description='',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='Oscar M. Lage',
    author_email='info@oscarmlage.com',
    url='https://oscarmlage.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires
)
