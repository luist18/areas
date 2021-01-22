#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
<<<<<<< HEAD

apt-get update
apt-get install -y git

sh $DIR/requirements/system_requirements.sh

pip3 install -U -r $DIR/requirements/py_requirements.txt

export MAST_PATH=$DIR/src/main.py
=======

apt-get update
apt-get install -y git

sh $DIR/requirements/system_requirements.sh

pip3 install -U -r $DIR/requirements/py_requirements.txt
>>>>>>> 8c1bb0800e47a607f5a3b19a2b2b5e832637508b

echo 'alias mast="python3 '$DIR'/src/main.py"' >> ~/.bashrc
