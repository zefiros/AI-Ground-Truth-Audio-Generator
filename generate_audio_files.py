import os
import requests
import wave
from dotenv import load_dotenv

# --- Ρυθμίσεις ---
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Voice ID για τον "Antoni" (multilingual v2)
MODEL_ID = "eleven_multilingual_v2" # Model to support Ελληνικά
INPUT_FILE = "ground_truth.txt"    # file with 100 sentage
OUTPUT_DIR = "audio_files_ground_truth" # Export wav files

# API URL parameter wit correct format voice
API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format=pcm_16000"

# Headers for check of id
HEADERS = {
    "Accept": "audio/wav",
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY
}

def create_audio_files():
    """
     Read the ground_truth.txt and create one .wav file for each sentage 
    we used the ElevenLabs API, the correct format (PCM 16kHz).
    """
    
    # 1. Creat the output folder if does not exist 
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print(f" Start the creation of sound files in folder '{OUTPUT_DIR}'...")
    
    # 2. Open end read the file ground truth
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"ERROR: The file  '{INPUT_FILE}' not found.")
        return

    file_counter = 1
    
    # 3. Executer evry line 
    for line in lines:
        text = line.strip()
        
        # Skip empty line and comment
        if not text or text.startswith("#"):
            continue
            
        print(f"Επεξεργασία γραμμής {file_counter}: \"{text[:50]}...\"")
        
        # 4. Payload for API
        data = {
            "text": text,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.0, # 0.0 = nutral/ptofetional style 
                "use_speaker_boost": True
            }
        }
        
        try:
            # 5. Call API
            response = requests.post(API_URL, headers=HEADERS, json=data, timeout=60)
            
            if response.status_code == 200:
                # 6. Correct save as WAV (PCM 16kHz, 16-bit, Mono)
                filename = f"{file_counter:03d}_audio.wav"
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                with wave.open(filepath, 'wb') as wav_file:
                    wav_file.setnchannels(1)       # 1 = Mono
                    wav_file.setsampwidth(2)       # 2 bytes = 16-bit
                    wav_file.setframerate(16000)   # 16kHz
                    wav_file.writeframes(response.content)
                    
                file_counter += 1
                
            else:
                print(f"  -> Error on API in Line: {text}. Status Code: {response.status_code}")
                print(f"     Answer: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"  -> Error Connection: {e}")

    print(f"\nComplete! Created Total {file_counter - 1} file voice.")

# --- Εκτέλεση του script ---
if __name__ == "__main__":
    if not ELEVENLABS_API_KEY:
        print("Error: The 'ELEVENLABS_API_KEY' is not found on .env file.")
    else:
        create_audio_files()