from collections import Counter
import string

from lxml import etree
from nltk import tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def parse_xml():
    root = etree.parse('news.xml').getroot()
    news_headers, news_texts = list(), list()
    for news in root[0]:
        for value in news:
            if value.get('name') == 'head':
                news_headers.append(value.text)
            elif value.get('name') == 'text':
                news_texts.append(value.text)

    return news_headers, news_texts


def get_most_common(text_string):
    # Tokenize & lemmatize
    tokens = sorted(tokenize.word_tokenize(text_string.lower()), reverse=True)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    # Sort by frequency
    lemmas_dict = dict(Counter(lemmas).most_common())
    # Get rid of punctuation and stopwords and keep only first 5 items
    most_common = list()
    for key in lemmas_dict.keys():
        if key not in stops and key not in list(string.punctuation):
            most_common.append(key)
            if len(most_common) == 5:
                break
    return ' '.join(most_common)


if __name__ == '__main__':
    headers, texts = parse_xml()
    lemmatizer = WordNetLemmatizer()
    stops = set(stopwords.words('english'))
    for header, text in zip(headers, texts):
        print(f'{header}:')
        print(get_most_common(text), end='\n\n')
