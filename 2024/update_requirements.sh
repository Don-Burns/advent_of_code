#!/bin/bash
# script to update requirements with pip-tools
set -xeuo pipefail
# strip extra index if present, since its a token for codeartifact
pip-compile --upgrade --no-emit-index-url requirements.in
pip-compile --upgrade --no-emit-index-url --output-file=requirements-dev.txt requirements-dev.in
