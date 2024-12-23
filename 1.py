import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "recording.wav"  # Replace with your file path

try:
    # Use SpeechRecognition to process the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print("Extracted Text:")
        print(text)
except Exception as e:
    print("Error:", e)
