import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

exe = Executable(
      script="build_origin.py",
      base="Win32GUI",
      targetName="zbrac.exe",
	  icon="res/icon.ico"
     )


setup(
    name='zBrac',
    version='1.0.3',
    url='https://github.com/seyhunsaral/zbrac',
    license='GNU GPL-3',
    author='Ali Seyhun Saral, Anna Marie Schroeter',
    author_email='seyhunsaral@gmail.com, schroeter@coll.mpg.de',
	executables=[exe],
    scripts=['build_origin.py']
    ) 

