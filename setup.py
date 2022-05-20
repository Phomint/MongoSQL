import setuptools
import subprocess
import codecs

gowork_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
)

setuptools.setup(
    name="mongudb",
    version=gowork_version,
    author="Patrick Amaral",
    author_email="patrick.dev.atom@gmail.com",
    description="Library to query like SQL",
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    url="https://github.com/Phomint/MongoSQL",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license='GPLv3',
    keywords=['databases', 'mongodb', 'query', 'sql'],
    install_requires=[
        "pymongo"
    ],
)