# !/bin/bash

dirname=$1

if [ ! -d "$dirname" ]
then
    mkdir ./$dirname && cd $dirname
    mkdir ./{application,config,deploy,tests}
    mkdir -p ./application/{controllers,models,static,static/css,static/js,static/image,templates}
    touch {manage.py,requirements.txt,README.md}
    touch ./application/{__init__.py,extensions.py}
    touch ./application/{controllers/__init__.py,models/__init__.py}
    touch ./application/{static/css/style.css,templates/404.html,templates/base.html,templates/index.html}
    touch ./{config/__init__.py,tests/__init__.py}
    echo "File created"
else
    echo "File exists"
fi
