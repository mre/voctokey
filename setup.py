from setuptools import setup, find_packages
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requires = convert_deps_to_pip(pfile['packages'], r=False)
test_requires = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(name='voctokey',
      version='0.0.1',
      description='Keyboard control for voctocore',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Utilities',
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      keywords='keyboard shortcut',
      url='http://github.com/mre/voctokey',
      author='Matthias Endler',
      author_email='matthias-endler@gmx.net',
      license='Apache',
      packages=find_packages(),
      install_requires=requires,
      tests_require=test_requires,
      entry_points={
          'console_scripts': ['voctokey=voctokey.__main__:main'],
      },
      include_package_data=True,
      zip_safe=False)
