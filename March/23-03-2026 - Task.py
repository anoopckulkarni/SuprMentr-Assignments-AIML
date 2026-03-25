from gensim.models import Word2Vec
import re

sentences = [
    "The players are training hard for the big football match",
    "Cricket is a popular sport played with a bat and ball",
    "The coach gave a motivating speech before the game started",
    "The team won the championship trophy after a tough season",
    "Athletes need a healthy diet and consistent exercise",
    "The stadium was packed with fans cheering for their team",
    "Running and swimming are excellent forms of cardio exercise",
    "The referee blew the whistle to start the second half",
    "Scoring a goal in the final minute is an amazing feeling",
    "Basketball players practice their shooting skills every day",
    "The Olympics feature athletes from every country in the world",
    "A good captain leads the team with confidence and skill",
    "Tennis matches can last for several hours on the court",
    "The gold medal is the highest honor for any Olympic athlete",
    "Winning requires both physical strength and mental toughness",
    "The crowd went wild when the player scored the winning point"
]

processed_data = [re.sub(r'[^\w\s]', '', s).lower().split() for s in sentences]

model = Word2Vec(sentences=processed_data, vector_size=50, window=3, min_count=1, workers=4)

word_to_check = "team"
print(f"Vector for '{word_to_check}' (first 10 dimensions):")
print(model.wv[word_to_check][:10]) 
target_word = "player"
print(f"\nWords most similar to '{target_word}':")
similar_words = model.wv.most_similar(target_word, topn=5)
for word, score in similar_words:
    print(f"{word}: {score:.4f}")