import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
duration = 30  # seconds
sample_rate = 44100  # Sampling rate (samples per second)

print("Recording...")
# Record audio
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
sd.wait()  # Wait until the recording is finished
print("Recording completed.")

# Save as a WAV file
output_file = "recording.wav"
write(output_file, sample_rate, audio_data)
print(f"Audio saved to {output_file}")
