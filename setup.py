try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

os_files = [
    ('/etc/init.d',['bin/devcontestd']),
]

setup(
    name='DevContest',
    version='0.4',
    description='Web interface for developers contests. Python, C, Pascal, PHP, Perl, Java',
    author='Juda Kaleta',
    author_email='juda.kaleta@gmail.com',
    url='http://github.com/yetty/DevContest/tree/0.3',
    license='GPL2',
    install_requires=[
        "Pylons==0.9.7",
        "routes==1.11",
        "SQLAlchemy>=0.5",
        "Pygments>=1.3.0",
        "webob==1.0.8",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'devcontest': ['i18n/*/LC_MESSAGES/*.mo']},
    message_extractors={'devcontest': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
            ('public/**', 'ignore', None)]},
    zip_safe=True,
    paster_plugins=['PasteScript', 'Pylons'],
    data_files = os_files,
    entry_points="""
    [paste.app_factory]
    main = devcontest.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
