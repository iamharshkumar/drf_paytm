import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='drf_paytm',
    version=__import__('drf_paytm').__version__,
    author=__import__('drf_paytm').__author__,
    author_email="pypidev@civilmachines.com",
    description="PayTM Integration based on Django REST Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=__import__('drf_paytm').__license__,
    url="https://github.com/101Loop/drf_paytm",
    python_requires=">=3.4",
    install_requires=open('requirements.txt').read().split(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP'
    ),
)
