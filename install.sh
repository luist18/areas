#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

apt-get update
apt-get install -y git

sh $DIR/requirements/system_requirements.sh

pip3 install -U -r $DIR/requirements/py_requirements.txt

echo 'alias mast="python3 '$DIR'/src/main.py"' >> ~/.bashrc
