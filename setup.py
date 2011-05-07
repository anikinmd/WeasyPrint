"""
WeasyPrint
----------

WeasyPrint converts web documents (HTML, CSS, SVG, ...) to PDF.

See the documentation at http://weasyprint.org/

"""

from setuptools import setup

setup(
    name='WeasyPrint',
    version='0.1dev',
    url='http://weasyprint.org/',
    license='GNU Affero General Public License',
    description='WeasyPrint converts web documents to PDF.',
    long_description=__doc__,
    packages=['weasy'],
    zip_safe=False,
    install_requires=[
        'lxml',
        'cssutils',
        'Attest',
        # Tricky to compile: 'pycairo', 'PyGTK',
        # Not on PyPI: 'rsvg',
    ],
    test_loader='attest:FancyReporter.test_loader',
    test_suite='weasy.tests.tests',
)
