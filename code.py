import webbrowser

# Emotion to Emojis
emoji_to_emotion = {
    "laughter": ["🤣","😂"],
    "happy":["😊","😀","😋","😚","🤗","😌","😝"],
    "confident":["😎"],
    "neutral":["😕","😐","😶","🫥"],
    "mad":["🤯","😖","😤","😬","😵","😵‍💫"],
    "sad":["😭","😔","😩","😞","😟"],
    "angry":["😡","😠"],
    "thinking about money":["🤑","💸","💰","💵","💳","💲"],
    "love":["❤️","🩷","🧡","💛","💚","💙","🩵","💜","🤎","💕","💞","💗","💓","💖","💘","💝","💌","💟"],
    "calm":["😴"],
    "party":["🪩"]
}

# Emotion related Song
emotion_to_song = {
    "laughter": "https://youtu.be/05TA9jNnCdU",
    "happy": "https://www.youtube.com/watch?v=6vKucgAeF_Q",
    "confident": "https://youtu.be/jMfvlh0tjyo",
    "neutral": "https://www.youtube.com/watch?v=MRtRcTfszjY",
    "mad": "https://www.youtube.com/watch?v=ABG0gQ9czvk",
    "sad": "https://youtu.be/z-diRlyLGzo",
    "angry": "https://youtu.be/p9DQINKZxWE",
    "thinking about money": "https://youtu.be/XsOPuQ9Z7Eo",
    "love": "https://www.youtube.com/watch?v=K-Ts-NFR62o",
    "calm": "https://www.youtube.com/watch?v=tyWMCwIRLVs",
    "party": "https://www.youtube.com/watch?v=TFTnJzWRTJ8"
}

# taking Input
emoji = input("Enter an emoji: ")

# Finding emotion
found = False

for emotion, emojis in emoji_to_emotion.items():
    if emoji in emojis:
        print(f"Detected Emotion: {emotion}")
        
        song = emotion_to_song[emotion]
        print("Playing your song... 🎶")
        
        webbrowser.open(song)
        found = True
        break

if not found:
    print("Emoji not recognized. SORRY!")
