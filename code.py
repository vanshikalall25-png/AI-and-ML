# AI-Based Emoji Emotion + Music Player


import webbrowser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# EMOJI DATA (converted to dataset)


emoji_to_emotion = {
    "laughter": ["🤣","😂"],
    "happy":["😊","😀","😋","😚","🤗","😌","😝"],
    "confident":["😎"],
    "neutral":["😕","😐","😶","🫥"],
    "mad":["🤯","😖","😤","😬","😵","😵‍💫"],
    "sad":["😭","😔","😩","😞","😟"],
    "angry":["😡","😠"],
    "money":["🤑","💸","💰","💵","💳","💲"],
    "love":["❤️","💖","💕","💘","💝"],
    "calm":["😴"],
    "party":["🪩"]
}

#  CREATE DATASET FOR ML


texts = []
labels = []

for emotion, emojis in emoji_to_emotion.items():
    for e in emojis:
        texts.append(e)
        labels.append(emotion)

#TEXT TO NUMERIC


vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(texts)


# TRAIN MODEL 

model = MultinomialNB()
model.fit(X, labels)


# STEP 5: SONG LINKS (same as yours)


emotion_to_song = {
    "laughter": "https://youtu.be/05TA9jNnCdU",
    "happy": "https://www.youtube.com/watch?v=6vKucgAeF_Q",
    "confident": "https://youtu.be/jMfvlh0tjyo",
    "neutral": "https://www.youtube.com/watch?v=MRtRcTfszjY",
    "mad": "https://www.youtube.com/watch?v=ABG0gQ9czvk",
    "sad": "https://youtu.be/z-diRlyLGzo",
    "angry": "https://youtu.be/p9DQINKZxWE",
    "money": "https://youtu.be/XsOPuQ9Z7Eo",
    "love": "https://www.youtube.com/watch?v=K-Ts-NFR62o",
    "calm": "https://www.youtube.com/watch?v=tyWMCwIRLVs",
    "party": "https://www.youtube.com/watch?v=TFTnJzWRTJ8"
}


# STEP 6: USER INPUT

emoji = input("Enter an emoji: ")

# Convert input
input_vector = vectorizer.transform([emoji])

# Predict emotion using AI
prediction = model.predict(input_vector)[0]

print("Detected Emotion:", prediction)

# Play song
if prediction in emotion_to_song:
    print("Playing your song... 🎶")
    webbrowser.open(emotion_to_song[prediction])
else:
    print("No song found.")
