#!/bin/bash

apt-get install -y git

sh requirements/system_requirements.sh

pip3 install -U -r /requirements/py_requirements.txt

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo 'alias mast="python3 '$DIR'/src/main.py"' >> ~/.bashrc