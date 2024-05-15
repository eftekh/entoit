#!/bin/bash
set -ex
cd `dirname $0`

python3 -m venv --upgrade-deps --clear --prompt entoit .entoit
source .entoit/bin/activate
python -m pip install -r ci/requirements.txt
python -m pip install -r backend/requirements.txt
deactivate
