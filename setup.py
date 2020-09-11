import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Query string parser",
    version="1.0.0",
    license='GPL v3',
    author="Riccardo Curcio",
    author_email="rcurcio@coloombus.com",
    description="Query string parser like php",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coloombus/query-string-parser.git",
    download_url = 'https://github.com/coloombus/query-string-parser/archive/develop.zip',
    packages=setuptools.find_packages(),
    keywords = [
        'query string',
        'http',
        'coloombus'
    ],
    install_requires=['typing', 'querystring_parser', 'OrderedDict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
