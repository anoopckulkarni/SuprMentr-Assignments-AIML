import re
STOPWORDS = {"is", "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "with", "was", "were"}

def text_cleaner(text):

    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    cleaned_words = [w for w in words if w not in STOPWORDS]
    return " ".join(cleaned_words)

test_sentences = [
    "The movie was AMAZING!!! I loved it.",
    "Is the food in the kitchen ready for the party?",
    "Wait... was that a ghost or an alien with a hat?"
]

print(f"{'Original':<50} | {'Cleaned'}")
print("-" * 85)
for sent in test_sentences:
    print(f"{sent:<50} | {text_cleaner(sent)}")