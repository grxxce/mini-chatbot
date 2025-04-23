import openai
import pyaudio
import wave as wv
import struct
import math
import time
import google.cloud.texttospeech as tts

openai.api_key = OPENAI_APIKEY

chatGPT = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role': 'system', 'content': "You are a CPT therapist who introduces themselves as Aimy."},
        {'role': 'user', 'content': "Who are you? Give me a brief intro"}]
    )
intro = chatGPT['choices'][0]['message']['content']
print(intro)
time.sleep(5)
print("go ahead and ask away!")


def rms(data):
    count = len(data) / 2
    format = "%dh" % count
    shorts = struct.unpack(format, data)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0 / 32768)
        sum_squares += n * n
    return math.sqrt(sum_squares / count)

silence_threshold = 0.05  # Adjust this value based on your environment and microphone sensitivity
silence_duration = 1  # Adjust the duration (in seconds) of silence required to stop recording
consecutive_silence_frames = int(silence_duration * 44100 / 1024)

silence_counter = 0
try: 
    while True:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        try:
            while True:
                data = stream.read(1024)
                rms_value = rms(data)
                if rms_value < silence_threshold:
                    silence_counter += 1
                    if silence_counter >= consecutive_silence_frames:
                        silence_counter = 0
                        break
                else:
                    silence_counter = 0
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

        audio_file = open("myrecording.wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message = transcript["text"]
        print("You said: ", message)
        print("")

        chatGPT = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': "Be the best CPT therapist in the world. Prompt conversation, have compassion, and be understanding. Use mentalization as a therapy tool."},
            {'role': 'user', 'content': message}]
        )
        response = chatGPT['choices'][0]['message']['content']
        print("Chat GPT: ", response)
except KeyboardInterrupt:
    chatGPT = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role': 'system', 'content': "Be the best CBT therapist in the world. Prompt conversation, have compassion, and be understanding. Use mentalization as a therapy tool."},
        {'role': 'user', 'content': "Close our therapy session in 1 sentence by providing a summary of what we worked on."}]
    )
    outro = chatGPT['choices'][0]['message']['content']
    print(outro)
    time.sleep(15)
