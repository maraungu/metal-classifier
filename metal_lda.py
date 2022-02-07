from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def metal_lda(df, stop_words, n_components):
    count = CountVectorizer(stop_words=stop_words,
                            max_df=.1,
                            max_features=5000)
    X = count.fit_transform(df['lyrics'].values)
    lda = LatentDirichletAllocation(n_components=n_components,
                                    random_state=123,
                                    learning_method='batch')
    X_topics = lda.fit_transform(X)
    return lda, count
