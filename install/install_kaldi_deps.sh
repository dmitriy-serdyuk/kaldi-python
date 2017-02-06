#!/usr/bin/env sh
if [ -f $HOME/kaldi/KALDI_DEPS_INSTALLED ]; then
    echo "kaldi deps are installed"
    exit 0
fi
git clone https://github.com/kaldi-asr/kaldi.git $HOME/kaldi
cd $HOME/kaldi/tools
./extras/check_dependencies.sh
make
cd $HOME/kaldi/tools
./extras/install_openblas.sh
touch $HOME/kaldi/KALDI_DEPS_INSTALLED
exit 1
