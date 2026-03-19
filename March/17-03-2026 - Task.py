import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = {
    'review': [
        'I absolutely loved this movie, the acting was brilliant',
        'A complete waste of time and money, do not watch',
        'It was an okay film, not great but not terrible either',
        'The cinematography was stunning and the plot was deep',
        'I hated every minute of this boring film',
        'The story was average, nothing special to mention',
        'Highly recommended for fans of the genre, truly a masterpiece',
        'Worst experience ever, I left the theater early',
        'It had some good moments but overall it was just fine',
        'An incredible journey with fantastic character development',
        'Poor script and even worse directing, stay away',
        'Middle of the road performance, nothing stands out',
        'The best movie I have seen this year, simply amazing',
        'Garbage plot and wooden acting throughout',
        'A decent watch if you have nothing else to do',
        'Beautifully shot with a moving soundtrack',
        'The pacing was slow and the ending was disappointing',
        'It was a fair movie for a rainy afternoon',
        'Exhilarating action sequences and a great cast',
        'Total disaster, I regret watching it',
        'It was a standard rom-com with no surprises'
    ],
    'sentiment': [
        'Positive', 'Negative', 'Neutral', 'Positive', 'Negative', 
        'Neutral', 'Positive', 'Negative', 'Neutral', 'Positive', 
        'Negative', 'Neutral', 'Positive', 'Negative', 'Neutral', 
        'Positive', 'Negative', 'Neutral', 'Positive', 'Negative', 'Neutral'
    ]
}

df = pd.DataFrame(data)

X = df['review']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

new_reviews = [
    "It was a breathtaking experience from start to finish",
    "It was neither good nor bad, just a typical movie",
    "I cannot believe how bad the writing was"
]
new_tfidf = tfidf.transform(new_reviews)
predictions = model.predict(new_tfidf)

for review, pred in zip(new_reviews, predictions):
    print(f"Review: {review} -> Sentiment: {pred}")