import pyttsx3

# Initialize the converter
engine = pyttsx3.init()

# Open and read the text file
with open('testfile.txt', 'r') as file:
    text = file.read()

# Convert text to speech
engine.say(text)
engine.runAndWait()
