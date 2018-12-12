import setuptools
from os import path
from io import open
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='zbrac',
    python_requires='>3.6.0',
    version='1.0.4',
	packages=['zbrac'],
    url='https://github.com/seyhunsaral/zbrac',
    license='GNU GPL-3',
    author='Ali Seyhun Saral, Anna Marie Schroeter',
    author_email='seyhunsaral@gmail.com, schroeter@coll.mpg.de',
    description='A multilanguage tool for zTree',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown', install_requires=['openpyxl>=2.5.8','PyQt5>=5.11.3','PyQt5-sip>=4.19.13','PyQt5.sip>=4.19.13','urllib3>=1.24.1','XlsxWriter>=1.1.1'],
    entry_points = {'console_scripts': ['zbrac=zbrac.start:main'],},
    zip_safe=False
)
