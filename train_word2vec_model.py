# -*- coding: utf-8 -*-
# train_word2vec_model.py用于训练模型

import logging
import os.path
import sys

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__=='__main__':
  program = os.path.basename(sys.argv[0])
  logger = logging.getLogger(program)

  logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
  logging.root.setLavel(level=logging.INFO)
  logging.info("running %s" % ' '.join(sys.argv))

  if len(sys.argv) < 4:
    print global()['__doc__'] % locals()
    sys.exit(1)

  inp,outp,outp2 = sys.argv[1:4]

  model = Word2Vec(LineSentence(inp),size=128,window=5,min_count=5)

  model.save(outp)
  model.save_word2vec_format(outp2,binary=false)