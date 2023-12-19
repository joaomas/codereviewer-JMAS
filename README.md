# codereviewer

Tool for automated Fortran Code Review based on GCC rules

Language used: Python

Programming paradigm -Object-oriented programming (OOP) 


> codereviewer
     README.md
     LICENSE
     src/


### Installation instructions

- Check for java installed (default-jre). If not installed: 
`sudo apt install default-jre`

- Create and activate a virtual env: 
~~~
python3 -m venv .venv
source .venv/bin/activate
~~~

- Install requirements:
~~~
make init
~~~

- Test

~~~
make test
~~~