import gensim
import jieba
import random

import numpy as np
from scipy.linalg import norm
import jieba.posseg as psg
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors

from db_tools.sentence import Sentence


def vector_similarity(id1, id2, vecs, stopwords, tf_idf, keys, language):
    """
    Calculate similarity between 2 sentences
    Parameters:
        id1, id2: Integer, sentence id (column index).
        vecs: word_vectors file.
        stopwords: a list containing stopwords to ignore when getting the sentence vector.
        tf_idf: tf-idf matrix
        keys: sorted words list of all docs
    Return:
        A float, as the similarity of Sentence id1 and id2.
    """

    def sentence_vector_with_tf(keys, tf):
        v = np.zeros(64) if language == "ch" else np.zeros(300)
        for i, t in enumerate(tf):
            if t != 0:
                word = keys[i]
                # print(word, ":", t)
                if word not in stopwords and word in vecs.vocab:
                    v += t * vecs[word]
        return v

    tf1 = tf_idf[:, id1]
    tf2 = tf_idf[:, id2]
    v1, v2 = sentence_vector_with_tf(keys=keys, tf=tf1), sentence_vector_with_tf(keys=keys, tf=tf2)
    eu_dist = np.linalg.norm(v1 - v2)
    return eu_dist


def get_min_WCD(id, vecs, stopwords, tf_idf, keys, ref_num, language):
    min_vecsim = vector_similarity(id1=0, id2=id, vecs=vecs, stopwords=stopwords,
                                   tf_idf=tf_idf, keys=keys, language=language)
    for ref_index in range(ref_num):
        min_vecsim = min(min_vecsim, vector_similarity(id1=ref_index, id2=id, vecs=vecs,
                                                       stopwords=stopwords, tf_idf=tf_idf,
                                                       keys=keys, language=language))
    return min_vecsim





