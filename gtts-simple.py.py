from gtts import gTTS

# Step 1: Input text (in German)
text = input("Gib den deutschen Text ein: ")

# Step 2: Set language to German or any language of your choice
language = 'de'

# Step 3: Convert to speech
tts = gTTS(text=text, lang=language)

# Step 4: Save to file
filename = "google.mp3"
tts.save(filename)

print(f"Die Audiodatei wurde gespeichert als '{filename}'")
