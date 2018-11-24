:: For proper executable generation, we install
:: zBrac as a package and then generate exe file with cxfreeze 
pip uninstall zbrac -y
pip install ./src/zbrac --user
python setup_cxfreeze.py build 
