#!/usr/bin/env bash
pyrcc5 ./res/resources.qrc -o ./src/zbrac/zbrac/resources_rc.py
pyuic5 --from-imports ./ui/mainwindow.ui -o ./src/zbrac/zbrac/mainwindow.py
python src/zbrac/run.py  
