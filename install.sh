#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

apt-get update
apt-get install -y git

sh $DIR/requirements/system_requirements.sh

pip3 install -U -r $DIR/requirements/requirements.txt

export MAST_PATH=$DIR/arm63_tester/main.py

echo 'alias mast="python3 '$DIR'/src/main.py"' >> ~/.bashrc
