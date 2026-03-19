import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(corpus)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

print("--- 1. BAG OF WORDS MATRIX ---")
bow_df = pd.DataFrame(
    bow_matrix.toarray(), 
    columns=bow_vectorizer.get_feature_names_out(),
    index=corpus
)
print(bow_df)

print("\n--- 2. TF-IDF MATRIX ---")
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(), 
    columns=tfidf_vectorizer.get_feature_names_out(),
    index=corpus
)
print(tfidf_df.round(2))
print("\n--- COMPARISON ---")
print("Bag of Words: Uses integers (0, 1, 2). It only cares about frequency.")
print("TF-IDF: Uses decimals (0.0 to 1.0). It penalizes common words like 'this' or 'movie'")
print("and gives higher scores to unique sentiment words like 'amazing' or 'terrible'.")