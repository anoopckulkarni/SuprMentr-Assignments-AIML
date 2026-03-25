import re

messy_sentences = [
    "The movie was soooooo goooood!!! 😍",
    "I h8 it when the wifi drops out.",
    "Worst. Day. Ever. 🙄 #fml",
    "The food was expensive af but worth it.",
    "Cud u plz chck the report asap?"
]

def clean_text(text):
    text = text.lower()
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'(.)\1+', r'\1\1', text)
    return text.strip()

print("--- Original vs Cleaned ---")
for sent in messy_sentences:
    print(f"Original: {sent}")
    print(f"Cleaned : {clean_text(sent)}\n")