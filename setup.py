from setuptools import setup

setup(name='course catalog',
    version='0.1',
    description='A project for Worthwhile Application',
    url='github.com/notyoyoma',
    author='Marty Naselli',
    author_email='marty.naselli@gmail.com',
    license='wtfpl',
    packages=['courses'],
    install_packages=[
        'Pillow',
        'django-bootstrap3',
    ],
    zip_safe=False
)
