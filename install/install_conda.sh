#!/usr/bin/env bash
if [ -f $HOME/miniconda/CONDA_INSTALLED ]; then
    echo "miniconda is installed"
    exit 0
fi

rm -r $HOME/miniconda

if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then
    wget -q http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
else
    wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
fi
chmod +x miniconda.sh
./miniconda.sh -b -p $HOME/miniconda
touch $HOME/miniconda/CONDA_INSTALLED
exit 1
