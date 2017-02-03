#!/usr/bin/env sh
if [ -f $HOME/kaldi/KALDI_INSTALLED ]; then
    echo "kaldi dir is not empty"
    exit 0
fi
cd $HOME/kaldi/src
export CXXFLAGS=-fPIC:$CXXFLAGS
./configure --static --use-cuda=no --openblas-root=$HOME/kaldi/tools/OpenBLAS/install
make depend
make -j 4
touch $HOME/kaldi/KALDI_INSTALLED
exit 1
