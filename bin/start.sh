#!/usr/bin/env bash

set -e

THIS_DIR=$(dirname "$0")
cd ${THIS_DIR}
cd ..


FLASK_APP=flaskr FLASK_ENV=development flask run