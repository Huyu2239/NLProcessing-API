import MeCab
import json
from gensim.models import KeyedVectors


wv = KeyedVectors.load_word2vec_format('./wiki.vec.pt', binary=True)
def get_similar_words(word):
    try:
        results = wv.most_similar(positive=[word], topn=5)
    except Exception:
        return []
    return [result[0] for result in results]


def convert_to_ninja(text):
    with open('./word_dict.json') as f:
        word_dict = json.load(f)
    t = MeCab.Tagger('-O wakati')
    origin_text_words = t.parse(text).split()
    for i, word in enumerate(origin_text_words):
        if word in word_dict.keys():
            origin_text_words[i] = word_dict[word]
    return "".join(origin_text_words)
