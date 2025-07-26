import pyaudio
import time
import struct

def test_microphone():
    print("🎤 Testing Microphone Input...")
    print("Speak into your microphone for 5 seconds...")
    
    # Audio settings
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    
    try:
        audio = pyaudio.PyAudio()
        
        # List available audio devices
        print("\n🔍 Available Audio Devices:")
        for i in range(audio.get_device_count()):
            device_info = audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                print(f"  Device {i}: {device_info['name']} (Input channels: {device_info['maxInputChannels']})")
        
        print(f"\n🎤 Recording for {RECORD_SECONDS} seconds...")
        print("Speak now!")
        
        # Start recording
        stream = audio.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK)
        
        max_volume = 0
        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            
            # Calculate volume level (simple method)
            values = struct.unpack(f'{CHUNK}h', data)
            volume = max(abs(v) for v in values)
            max_volume = max(max_volume, volume)
            
            # Show real-time volume
            if i % 10 == 0:  # Update every ~0.25 seconds
                volume_bar = "█" * min(int(volume / 1000), 30)
                print(f"Volume: {volume_bar} ({volume})", end='\r')
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        print(f"\n\n📊 Test Results:")
        print(f"Maximum volume detected: {max_volume}")
        
        if max_volume > 1000:
            print("✅ GOOD: Microphone is working and detecting audio!")
        elif max_volume > 200:
            print("⚠️  WEAK: Microphone detected but signal is low")
            print("   Try speaking louder or check microphone settings")
        else:
            print("❌ PROBLEM: No significant audio detected")
            print("   Check microphone permissions and device settings")
            
    except Exception as e:
        print(f"❌ Error testing microphone: {e}")
        print("This might be a permission or driver issue")

if __name__ == "__main__":
    test_microphone()
