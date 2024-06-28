#!/usr/bin/bash
# Instalação open-fortran-parser (ubuntu 22.04)
#    caso não tenha o Java instalado:
#       sudo apt install default-jre              
#    $pip install open-fortran-parser

/usr/bin/python3 -m open_fortran_parser ../code_under_test/teste.F90 ../xml/saida.xml

