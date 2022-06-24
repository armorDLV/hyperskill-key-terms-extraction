from collections import Counter

from lxml import etree
from nltk import tokenize


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


def get_most_common(string):
    token = sorted(tokenize.word_tokenize(string.lower()), reverse=True)
    most_common = dict(Counter(token).most_common(5)).keys()
    return ' '.join(most_common)


if __name__ == '__main__':
    headers, texts = parse_xml()
    for header, text in zip(headers, texts):
        print(f'{header}:')
        print(get_most_common(text), end='\n\n')
