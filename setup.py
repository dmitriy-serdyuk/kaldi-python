#!/usr/bin/env python

import os
from distutils.core import setup
from distutils.command.build_py import build_py

class Make(build_py):
    def run(self):
        os.system("make")
        build_py.run(self)

setup(name='kaldi-python',
      version='1.0',
      description='Python interface for kaldi iterators',
      author='Jan Chorowski',
      url='https://github.com/janchorowski/kaldi-python',
      cmdclass={'build_py': Make},
      packages=['kaldi_io', 'kaldi_argparse'],
      package_dir={'kaldi_io': 'kaldi-python/kaldi_io',
                   'kaldi_argparse': 'kaldi-python/kaldi_argparse'},
      package_data={'kaldi_io': ['kaldi_io_internal.so']},
      scripts=['scripts/apply-global-cmvn.py',
               'scripts/compute-global-cmvn-stats.py',
               'scripts/copy-feats-padded.py',
               'scripts/show-wav-ali.py'],
      requires=['numpy'])