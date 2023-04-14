import openai
import pyaudio
import wave as wv
openai.api_key = "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"
# import pydub
print("Hi, I'm mini-siri! Start talking to ask any question, and press '^C' when you are done talking.")

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []

try:
    while True:
        data = stream.read(1024)
        frames.append(data)

except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wv.open("myrecording.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()

audio_file= open("myrecording.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript)
message = transcript["text"]
print("You said: ", message)
print("")

chatGPT = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {'role':'system', 'content': "Have a funny, snarky, quirky personality."},
    {'role':'user', 'content': message}]
)
response = chatGPT['choices'][0]['message']['content']
print("Chat GPT: ", response)
 