#!/usr/bin/env python

import os
from distutils.core import setup
from distutils.command.build import build

class Make(build):
    def run(self):
        exit_code = os.system("make")
        if exit_code != 0:
            raise Exception("error during building")
        build.run(self)

setup(name='kaldi-python',
      version='1.0',
      description='Python interface for kaldi iterators',
      author='Jan Chorowski',
      url='https://github.com/janchorowski/kaldi-python',
      cmdclass={'build': Make},
      packages=['kaldi_io', 'kaldi_argparse'],
      package_data={'kaldi_io': ['kaldi_io_internal.so']},
      scripts=['scripts/apply-global-cmvn.py',
               'scripts/compute-global-cmvn-stats.py',
               'scripts/copy-feats-padded.py',
               'scripts/show-wav-ali.py'],
      requires=['numpy'])
