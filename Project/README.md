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
- Working microphone and speakers/headphones
- ElevenLabs account (free tier available with 10,000 credits = ~15 minutes)

## 🔧 Setting Up ElevenLabs

### 1. Create ElevenLabs Account
1. Sign up at [ElevenLabs](https://elevenlabs.io/)
2. Go to **"Conversational AI"** → **"Agents"**
3. Click **"Start from blank"** to create a new agent

![ElevenLabs Dashboard](https://github.com/user-attachments/assets/2faf577f-b9d3-4ec4-8a58-df6ee1e3b9a0)

### 2. Configure Your Agent
1. **Copy your Agent ID** from the agent page
2. Go to **"Security"** tab → Enable **"First message"** and **"System prompt"** overrides → Save
3. Go to your **Profile** → **"API Keys"** → Create new API key

![Agent Configuration](https://github.com/user-attachments/assets/2f3ef54e-0eab-456b-b651-e53924c83133)

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/elevenlabs-voice-assistant.git
cd elevenlabs-voice-assistant
```

### 2. Install Dependencies

**For Windows:**
```bash
pip install elevenlabs python-dotenv pyaudio
```

**For Linux:**
```bash
sudo apt install portaudio19-dev
pip install elevenlabs python-dotenv pyaudio
```

**For MacOS:**
```bash
brew install portaudio
pip install elevenlabs python-dotenv pyaudio
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root:
```env
AGENT_ID=your_agent_id_here
API_KEY=sk_your_api_key_here
```

⚠️ **Important:** No spaces around the `=` symbol in `.env` files!

### 4. Test Your Setup
```bash
# Test your microphone first
python test_microphone.py

# Run the voice assistant
python Voice_assistent.py
```

## 📁 Project Structure

```
elevenlabs-voice-assistant/
├── Voice_assistent.py      # Main voice assistant application
├── test_microphone.py      # Audio input testing utility
├── .env                    # Environment variables (create this file)
├── .gitignore             # Git ignore rules
└── README.md              # This documentation
```

## 🎯 How to Use

### 1. Start the Assistant
```bash
python Voice_assistent.py
```

### 2. Look for Confirmation
```
🎤 Voice Assistant is ACTIVE!
✅ Session active! Talk now!
🔴 LIVE - Voice assistant is listening...
```

### 3. Start Talking
- Speak clearly and naturally
- The AI will respond with voice
- Have a natural conversation!

### 4. Stop the Session
Press `Ctrl+C` to end the conversation

## 🛠️ Configuration & Optimization

### Audio Models Used
- **TTS Model:** `eleven_turbo_v2_5` (fast, high-quality speech synthesis)
- **STT Model:** `eleven_english_sts_v2` (accurate speech recognition)

### Microphone Optimization
- **External microphones recommended** for better voice detection
- **Test audio levels:** Run `python test_microphone.py`
- **Optimal volume:** 15,000-25,000+ for reliable detection
- **Built-in laptop mics:** Often too quiet, may cause detection issues

### Audio Processing Specs
- **Sample Rate:** 44.1kHz
- **Channels:** Mono (1 channel)  
- **Format:** 16-bit PCM
- **Processing:** Real-time WebSocket streaming

## 🔧 Troubleshooting

### ❌ Common Issues & Solutions

**🚨 "Text callbacks not working" - Conversation text not showing:**
```
✅ This is a known ElevenLabs SDK limitation
✅ Your assistant IS working if you hear audio responses
✅ Audio conversation works perfectly despite missing text
```

**🎤 "Voice not detected" - Assistant not responding:**
```bash
# Test your microphone
python test_microphone.py

# Solutions:
• Ensure microphone volume > 15,000
• Use external microphone instead of laptop built-in
• Check microphone permissions in Windows settings
• Speak closer to microphone
```

**🔑 "Authentication errors":**
```bash
# Check your .env file:
• Verify AGENT_ID is correct (no quotes needed)
• Verify API_KEY starts with sk_ (no quotes needed)
• Ensure no spaces around = symbol
• Check ElevenLabs dashboard for agent status
```

**💻 "Installation issues":**
```bash
# Windows: Install Visual C++ Build Tools if pyaudio fails
# Linux: sudo apt install portaudio19-dev python3-dev
# MacOS: brew install portaudio
```

## 🎥 Recording Your Sessions

### Windows Built-in Tools
- **Game Bar:** Press `Windows + G` → `Windows + Alt + R` to record
- **Voice Recorder:** Use Windows Voice Recorder app for audio-only

### Third-party Options
- **OBS Studio** (Free, professional)
- **Audacity** (Free, audio-only)

## 📊 Technical Details

### Dependencies Explained
- **`elevenlabs`** - ElevenLabs Python SDK for conversational AI
- **`python-dotenv`** - Secure environment variable management  
- **`pyaudio`** - Real-time audio input/output handling
- **`threading`** - Multi-threaded session management and status updates

### How It Works
```
1. python-dotenv → Loads your API keys securely
2. elevenlabs → Connects to ElevenLabs using credentials
3. pyaudio → Captures your voice from microphone
4. elevenlabs → Sends voice to ElevenLabs for AI processing
5. elevenlabs → Receives AI response as synthesized speech
6. pyaudio → Plays AI response through speakers
7. threading → Shows status updates while conversation continues
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### How to Contribute
1. **Fork the repository** on GitHub
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** and test them thoroughly
4. **Commit your changes:** `git commit -m 'Add amazing feature'`
5. **Push to your branch:** `git push origin feature/amazing-feature`
6. **Open a Pull Request** with a clear description

### What We're Looking For
- 🐛 Bug fixes and improvements
- 📝 Documentation enhancements
- ✨ New features (please discuss first in issues)
- 🧪 Test improvements
- 🎨 UI/UX improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[ElevenLabs](https://elevenlabs.io/)** - For providing the amazing Conversational AI platform
- **Python Community** - For excellent audio processing libraries
- **Contributors** - Everyone who helped improve this voice assistant
- **Beta Testers** - Users who reported issues and provided feedback

## 📞 Support & Community

### Getting Help
- 🐛 **Bug Reports:** [Open a GitHub Issue](../../issues)
- 💡 **Feature Requests:** [Start a Discussion](../../discussions)
- ❓ **Questions:** [Check Discussions](../../discussions) or create a new one
- 📖 **Documentation:** [ElevenLabs Official Docs](https://elevenlabs.io/docs)

### Community Guidelines
- Be respectful and constructive
- Search existing issues before creating new ones
- Provide clear reproduction steps for bugs
- Test your contributions thoroughly

## 🚀 What's Next?

### Planned Features
- [ ] GUI interface for easier interaction
- [ ] Multi-language support
- [ ] Conversation history export
- [ ] Custom voice training integration
- [ ] Wake word detection
- [ ] Integration with other AI models

### Known Limitations
- ElevenLabs callback reliability issues (text display)
- Credit-based usage (free tier: ~15 minutes)
- Requires stable internet connection
- Platform-specific audio dependencies

---

**⭐ Star this repository if you found it helpful!**

**🔗 Share with friends who might enjoy building voice assistants!**

*Built with ❤️ using ElevenLabs Conversational AI*

---

> **Note:** This project requires ElevenLabs credits. The free tier provides 10,000 credits (~15 minutes of conversation). Additional credits can be purchased as needed.
