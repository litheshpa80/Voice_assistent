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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
