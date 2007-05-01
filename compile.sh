#!/bin/bash


pyuic4 main.ui -o main.py
pyuic4 about.ui -o ui_about.py
pyuic4 help.ui -o ui_help.py

pylupdate4 qphotosort.py main.ui -ts i18n/i18n_ca.ts
lrelease-qt4 i18n/i18n_ca.ts -qm i18n/i18n_ca.qm

pyrcc4 icons.qrc -o icons_rc.py
pyrcc4 i18n.qrc -o i18n_rc.py


