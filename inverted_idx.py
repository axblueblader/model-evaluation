from nltk.corpus import stopwords
from stop_words import get_stop_words
import tokenizer
import time


class InvertedIndex:
    def __init__(self):
        self.freq = 0
        self.postings = []
        self.classes = set()

    def _increase_freq(self):
        self.freq += 1

    def add_new_posting(self, doc_id):
        if(doc_id in self.postings):
            return
        else:
            self.postings.append(doc_id)
            self._increase_freq()


def remove_stop_words(word_list):
    stop_words = list(get_stop_words('en'))  # About 900 stopwords
    nltk_words = list(stopwords.words('english'))  # About 150 stopwords
    stop_words.extend(nltk_words)

    return [w for w in word_list if not w in stop_words]


def gen_inverted_idx(documents, class_map={}):
    print("Generating inverted index: ", end="")
    inverted_idx = {}
    terms_in_doc = {}
    start = time.time()
    for key in sorted(documents):
        terms = remove_stop_words(
            tokenizer.termize_doc(documents[key]))
        terms_in_doc[key] = remove_stop_words(
            tokenizer.tokenize_str(documents[key]))
        for term in terms:
            if (not (term in inverted_idx)):
                inverted_idx[term] = InvertedIndex()
            inverted_idx[term].add_new_posting(key)
        for class_name, doc_set in class_map.items():
            if (key in doc_set):
                inverted_idx[term].classes.add(class_name)
    end = time.time()
    print(end - start, "s")
    return inverted_idx, terms_in_doc


if __name__ == "__main__":
    result, terms_in_doc = gen_inverted_idx(
        {1: "abc xyz", 2: "qwe abc xyz", 3: "qwe", 4: "xyz"}, {"classA": {1, 3}, "classB": {3, 4}, "classC": {1, 2, 3}})
    for item in result:
        print(item, result[item].freq,
              result[item].postings, result[item].classes)
