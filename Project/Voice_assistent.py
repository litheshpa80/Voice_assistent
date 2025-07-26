import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

config = ConversationConfig(
    conversation_config_override={},
    extra_body={},
    dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
    print("DEBUG: print_agent_response called!")
    print(f"DEBUG: Response type: {type(response)}")
    print(f"DEBUG: Response content: {response}")
    print(f"🤖 Agent: {response}")
    print("Agent response received!")  # Debug

def print_interrupted_response(original, corrected):
    print("DEBUG: print_interrupted_response called!")
    print(f"DEBUG: Original: {original}, Corrected: {corrected}")
    print(f"🤖 Agent interrupted: {corrected}")
    print("Agent interruption received!")  # Debug

def print_user_transcript(transcript):
    print("DEBUG: print_user_transcript called!")
    print(f"DEBUG: Transcript type: {type(transcript)}")
    print(f"DEBUG: Transcript content: {transcript}")
    print(f"🎤 User: {transcript}")
    print("User transcript received!")  # Debug

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

print("🎤 Starting voice assistant...")
print("Speak now! Conversation will appear below:")
print("-" * 40)

try:
    print("DEBUG: About to start session...")
    conversation.start_session()
    print("DEBUG: Session started successfully")
    
    # Keep the session alive
    import time
    print("DEBUG: Keeping session alive...")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nStopping voice assistant...")
except Exception as e:
    print(f"ERROR: {e}")
    print(f"ERROR Type: {type(e)}")
    import traceback
    traceback.print_exc()
