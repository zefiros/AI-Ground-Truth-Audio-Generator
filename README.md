# 🎙️ AI Ground Truth Audio Generator

### Synthetic Voice Dataset Creation with ElevenLabs API

This repository contains a high-performance Python utility designed to automate the creation of high-quality audio datasets. It is specifically engineered to generate "Ground Truth" audio files for testing and benchmarking Speech-to-Text (STT) systems.

## 🚀 Key Features
- **ElevenLabs Multilingual V2 Integration:** Full support for high-fidelity Greek and multilingual synthetic speech.
- **Automated Batch Processing:** Iterates through text datasets (`ground_truth.txt`) to produce individual voice files.
- **Professional Audio Encoding:** Outputs PCM Wave files at **16kHz, 16-bit, Mono**—the industry standard for AI audio processing.
- **Customizable Voice Profiles:** Fine-tuned stability and similarity settings for neutral, professional-grade output.

## Author: Spyros Salouros

## Role: Principal AI Solutions Architect

## 🛠️ Architecture & Workflow
1. **Ingestion:** Reads raw text strings from a centralized ground truth file.
2. **Synthesis:** Streams PCM data from ElevenLabs API using the `Antoni` professional voice model.
3. **Encoding:** Manually constructs WAV headers and frames to ensure compatibility with STT engines (like Whisper or Wav2Vec2).


## 📋 Prerequisites
- Python 3.8+
- ElevenLabs API Key


  

## ⚙️ Installation & Setup



1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-audio-generator.git](https://github.com/your-username/ai-audio-generator.git)
   cd ai-audio-generator

### Install dependencies:
   
    pip install -r requirements.txt

##  Configure Environment Variables: Create a .env file in the root directory:

Code snippet
ELEVENLABS_API_KEY=your_actual_api_key_here

## 📊 Technical Specifications
Parameter	Setting
Model	eleven_multilingual_v2
Sample Rate	16,000 Hz
Bit Depth	16-bit
Channels	Mono
Format	WAV (PCM)

## 📖 Usage

### 1. Place your text dataset in ground_truth.txt (one sentence per line).

### 2. Run the generator:
Bash

python generate_audio_files.py

### 3. Your formatted .wav files will be available in the audio_files_ground_truth/ directory.




