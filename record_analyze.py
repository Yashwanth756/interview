import speech_recognition as sr
import pyttsx3
import spacy
import sounddevice as sd
from scipy.io.wavfile import write
import time
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight pre-trained model
nlp = spacy.load("en_core_web_md")


def listen_and_transcribe():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for up to 30 seconds, with a 10-second pause limit...")

        try:
            # Listen for up to 30 seconds total, with a 10-second pause limit
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=30)

            try:
                # Use Google Web Speech API to transcribe
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return None
            except sr.RequestError as e:
                # Handle request failure
                print(f"Could not request results from Google Web Speech API; {e}")
                return None
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for input.")
            return None
        except KeyboardInterrupt:
            print("Stopped listening.")
            return None


def text_to_speech(text):
    engine = pyttsx3.init() 
    engine.say(text)        
    engine.runAndWait()      
# text_to_speech(listen_and_transcribe())

def evaluate(sol, userSol):
    doc1 = nlp(sol)
    doc2 = nlp(userSol)
    return doc1.similarity(doc2)


def listenTranscribe(filename='1'):
    duration = 30  # seconds
    sample_rate = 44100  # Sampling rate (samples per second)

    print("Recording...")
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording completed.")

    # Save as a WAV file
    output_file = filename+".wav"
    write(output_file, sample_rate, audio_data)
    # print(f"Audio saved to {output_file}")

        # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    audio_file = filename+".wav"  # Replace with your file path

    try:
        # Use SpeechRecognition to process the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Extracted Text:")
            print(text)
            return text
    except Exception as e:
        print("Error:", e)
        return None
    
def evaluate2(sol, userSol):
    sentences = [sol, userSol]

    embeddings = model.encode(sentences)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    print(f'user sol is:\n{userSol}\nOrginal solution is:\n{sol}')
    print(f"Similarity: {similarity.item()}")
    return similarity.item()
# evaluate2('i love data science', 'machine learning')
