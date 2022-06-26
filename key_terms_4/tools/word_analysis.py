import string

from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class TermExtractor:
    """Tokenize, lemmatize and extract terms for a given text"""
    lemmatizer = WordNetLemmatizer()
    stops = set(stopwords.words('english'))

    def __init__(self, text):
        self.words = list()
        tokens = word_tokenize(text.lower())
        lemmas = list(TermExtractor.lemmatizer.lemmatize(token) for token in tokens)

        for lemma in lemmas:
            if pos_tag([lemma])[0][1] == 'NN':
                if lemma not in TermExtractor.stops and lemma not in list(string.punctuation):
                    self.words.append(lemma)

        self.processed_text = ' '.join(self.words)
