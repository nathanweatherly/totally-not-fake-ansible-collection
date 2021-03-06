#!/usr/bin/env bash
set -e
cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null

# Create collection documentation into temporary directory
rm -rf temp-rst
mkdir -p temp-rst
antsibull-docs collection \
    --use-current \
    --squash-hierarchy \
    --dest-dir temp-rst \
    nathanweatherly.totally_not_fake

# Copy collection documentation into source directory
# rsync -cprv --delete-after temp-rst/ rst/

# Build Sphinx site
# sphinx-build -M html rst build -c . -W --keep-going

