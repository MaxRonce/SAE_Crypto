from text_input import load_corpus, transform_to_caps, count_bigrams
import numpy as np

# =============================================================================

# CREATE BRIGRAMS (needed only the first time)
COUNT_BIGRAMS = False

corpus_filename = "../data/swann.txt"
bigrams_filename = "../data/bigrams.dat"

if COUNT_BIGRAMS:
    corpus = load_corpus(corpus_filename)
    corpus = transform_to_caps(corpus)
    count_bigrams(corpus, bigrams_filename, "../data/bigrams.png")

# =============================================================================

# LOAD BIGRAMS and build log(probability) matrix

bigrams = np.fromfile(bigrams_filename, dtype="int32").reshape(27, 27)
p = bigrams.astype('float') / np.tile(sum(bigrams.T), (27, 1)).T
p[np.isnan(p)] = 0
EPSILON = 1e-6
logp = np.log(p + EPSILON)


# =============================================================================