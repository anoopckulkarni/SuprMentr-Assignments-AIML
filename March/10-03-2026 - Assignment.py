import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    'text': [
        'Hey, are we still meeting for lunch at 12?',
        'WINNER! You have won a $1000 Walmart gift card. Click here now!',
        'Project update: The files are attached for your review.',
        'Urgent: Your account has been compromised. Verify your password.',
        'Can you pick up some milk on your way home?',
        'FREE entry to our prize draw. Text GO to 80100 to claim your spot!'
    ],
    'label': [0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

print("--- Spam Classifier Trained ---")

new_emails = [
    "Meeting rescheduled to 3pm", 
    "CONGRATULATIONS! You won a free prize. Click the link!"
]

new_emails_counts = vectorizer.transform(new_emails)
predictions = model.predict(new_emails_counts)

for email, pred in zip(new_emails, predictions):
    status = "SPAM" if pred == 1 else "HAM (Legit)"
    print(f"Email: '{email}' -> Result: {status}")