# 🎤 ElevenLabs Voice Assistant

A Python-based voice assistant powered by ElevenLabs Conversational AI that enables real-time voice conversations with advanced speech-to-text and text-to-speech capabilities.

## ✨ Features

- 🗣️ **Real-time Voice Conversations** - Natural voice interactions with AI agent
- 🎯 **ElevenLabs Integration** - High-quality speech synthesis and recognition
- 🔊 **Audio Quality Testing** - Built-in microphone testing and optimization
- 📝 **Conversation Logging** - Automatic text logging of conversations (when callbacks work)
- 🎛️ **Configurable Audio Models** - Support for multiple TTS/STT models
- 🔴 **Live Session Management** - Persistent conversation sessions with status updates

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- ElevenLabs API account and key
- Working microphone and speakers/headphones

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/elevenlabs-voice-assistant.git
   cd elevenlabs-voice-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install elevenlabs python-dotenv pyaudio
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   AGENT_ID=your_elevenlabs_agent_id
   API_KEY=your_elevenlabs_api_key
   ```

4. **Test your microphone:**
   ```bash
   python test_microphone.py
   ```

5. **Run the voice assistant:**
   ```bash
   python Voice_assistent.py
   ```

## 📁 Project Structure

```
elevenlabs-voice-assistant/
├── Voice_assistent.py      # Main voice assistant application
├── test_microphone.py      # Audio input testing utility
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🛠️ Configuration

### Audio Models
The assistant uses optimized ElevenLabs models:
- **TTS Model:** `eleven_turbo_v2_5` (fast, high-quality)
- **STT Model:** `eleven_english_sts_v2` (accurate speech recognition)

### Microphone Setup
- External microphones recommended for better voice detection
- Test audio levels with `test_microphone.py`
- Optimal volume levels: 15,000-25,000+ for reliable detection

## 🎯 Usage

1. **Start the assistant:**
   ```bash
   python Voice_assistent.py
   ```

2. **Wait for confirmation:**
   ```
   🎤 Voice Assistant is ACTIVE!
   ✅ Session active! Talk now!
   🔴 LIVE - Voice assistant is listening...
   ```

3. **Start talking:** Speak clearly and naturally to interact with the AI agent

4. **Stop the session:** Press `Ctrl+C` to end the conversation

## 🔧 Troubleshooting

### Common Issues

**🚨 Text callbacks not working:**
- This is a known ElevenLabs SDK limitation
- Audio conversations work perfectly despite missing text display
- The assistant is functioning correctly if you hear responses

**🎤 Voice not detected:**
- Run `python test_microphone.py` to check audio levels
- Ensure microphone volume is above 15,000
- Try using an external microphone instead of built-in laptop mic

**🔑 Authentication errors:**
- Verify your `.env` file contains correct `AGENT_ID` and `API_KEY`
- Check ElevenLabs dashboard for valid agent configuration

## 📊 Technical Details

### Dependencies
- `elevenlabs` - ElevenLabs Python SDK for conversational AI
- `python-dotenv` - Environment variable management
- `pyaudio` - Audio input/output handling
- `threading` - Session management and status updates

### Audio Processing
- **Sample Rate:** 44.1kHz
- **Channels:** Mono (1 channel)
- **Format:** 16-bit PCM
- **Real-time Processing:** WebSocket-based streaming

## 🎥 Recording Sessions

For session recording, use Windows built-in tools:
- **Game Bar:** Press `Windows + G`, then `Windows + Alt + R`
- **Voice Recorder:** Built-in Windows app for audio-only recording

# Setting Up the Environment
## Install Required Packages
Before we start, make sure you have Python installed. Then, install the required dependencies:

pip install elevenlabs elevenlabs[pyaudio] python-dotenv

Processing audio requires additional dependencies on Linux and MacOS:

For Linux, you need to install portaudio19:
sudo apt install portaudio19

For MacOS, you need to install portaudio:
brew install portaudio

## Setting up ElevenLabs
ElevenLabs provides a Conversational AI API that we will use to create our Voice Assistant.

🎤 The API records the user's voice through the microphone
🖨️ It processes it to know when the user has finished speaking or is interrupting the assistant
🤖 It calls an LLM model to generate a response
📈 It synthesizes the response into speech
🔊 It plays the synthesized speech through the speakers


Sign up at ElevenLabs and follow the instructions to create an account.

Once signed in, go to "Conversational AI".

<img width="1897" height="986" alt="image" src="https://github.com/user-attachments/assets/2faf577f-b9d3-4ec4-8a58-df6ee1e3b9a0" />


Go to "Agents".
<img width="1916" height="986" alt="image" src="https://github.com/user-attachments/assets/ad7fbae5-6354-4c6f-9b24-fd076e07689c" />

Click on "Start from blank".
<img width="1916" height="907" alt="image" src="https://github.com/user-attachments/assets/ec5dedff-4b12-4b19-b59c-5791c120226f" />

Create a .env file at the root of your project folder. We will use this file to store our API credentials securely. This way they won't be hardcoded in the script. In this .env file, add your Agent ID:
<img width="1902" height="902" alt="image" src="https://github.com/user-attachments/assets/23355a4f-a898-4854-8170-93e082fe8a75" />


AGENT_ID=your_agent_id

There shouldn’t be spaces around the = in a .env file.

Go to the "Security" tab, enable the "First message" and "System prompt" overrides, and save. This will allow us to customize the assistant's first message and system prompt using Python code.
<img width="1917" height="906" alt="image" src="https://github.com/user-attachments/assets/2f3ef54e-0eab-456b-b651-e53924c83133" />


Click on your profile and go to "API keys". Create a new API key and copy it to your .env file:
API_KEY="sk_XXX...XXX"

Important: Make sure to save your .env file after adding the credentials.
<img width="1916" height="911" alt="image" src="https://github.com/user-attachments/assets/29663cf9-8e06-43f6-96ef-79029089281d" />



ElevenLabs is now set up and ready to be used in our Python script!

Note: ElevenLabs works with a credit system. When you sign up, you get 10,000 free credits which amount to 15 minutes of conversation. You can buy more credits if needed.
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
