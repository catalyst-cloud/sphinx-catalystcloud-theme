from io import open
from setuptools import setup
from sphinx_catalystcloud_theme import __version__


setup(
    name='sphinx_catalystcloud_theme',
    version=__version__,
    url='https://github.com/catalyst-cloud/sphinx_catalystcloud_theme/',
    license='MIT',
    author='Amelia Cordwell',
    author_email='ameliacordwell@catalyst.net.nz',
    description='Catalyst Cloud theme for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_catalystcloud_theme'],
    package_data={'sphinx_catalystcloud_theme': [
        'theme.conf',
        '*.html',
        'static/*',
        'static/bootstrap/*/*.*',
        'static/cloudtheme/*/*.*',
        'static/cloudtheme/fonts/*/*.*',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'sphinx_catalystcloud_theme = sphinx_catalystcloud_theme',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
