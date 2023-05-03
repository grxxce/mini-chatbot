# Mini-Siri
Hello world! This is a "mini siri" program I put together with pure Python and OpenAI's Whisper and Chatbot APIs. The personality of the chatbot is completely programmable — see [Personalizing Mini-Siri](#-Personalizing-Mini-Siri)

I'm currently coding a frontend to make it more accessible. The end goal for this project is to create a therapy chatbot that can make CPT therapy more accessible for those who are in need.

Before that's ready, here are some startup instructions to set up this chatbot locally in your terminal. Have fun!

# Installation
### Clone the repository
```
git clone https://github.com/grxxce/mini-chatbot.git
```

### Install the dependencies
```
pip install openai
brew install portaudio
pip install pyaudio
npm install wave
```
Note that some of these dependencies may require ```sudo``` permision.

### Add your API key
Head to your [ChatGPT4](https://platform.openai.com/account/api-keys) account to create your API key. Create a ```config.py``` file and set ```api_key``` equal to the key you create.

### Run the program
```
python3 chatbot.py  
```
You're ready to go! Just follow the instructions in terminal and converse with ```Mini-Siri``` to your heart's desire 😄.


# Personalizing Mini-Siri
Modify [line 41](https://github.com/grxxce/mini-chatbot/blob/9cb764b23b9c79eb742e70d66db3d6ccfde73e4d/chatbot.py#L41) of chatbot.py to replace with any personality you desire!
