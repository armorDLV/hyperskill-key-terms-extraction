import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from tools import TermExtractor
from tools import XmlParser

if __name__ == '__main__':
    # Get headers and texts from xml file
    parser = XmlParser('news.xml')
    # Generate document collection for TF-IDF
    dataset = [TermExtractor(text).processed_text for text in parser.texts]
    # Vectorize
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(dataset)
    terms = vectorizer.get_feature_names_out()
    # Convert TF-IDF to a DataFrame and get top words for each text
    df = pd.DataFrame(tfidf_matrix.toarray())
    for idx_doc, row in df.iterrows():
        unique = row.sort_values(ascending=False).nlargest(5, 'all').unique()
        top_words_sorted = list()
        for value in unique:
            temp_word_list = list()
            for index, _ in row[row == value].items():
                temp_word_list.append(terms[index])
            temp_word_list.sort(reverse=True)
            top_words_sorted.extend(temp_word_list)
        # Print headers and top 5 words
        print(f'{parser.headers[idx_doc]}:')
        print(' '.join(top_words_sorted[:5]), end='\n\n')
