E.V.A. (Evolving Voice Assistant) is a locally hosted, AI-driven assistant that integrates a large language model (LLM) with advanced voice cloning. It listens to user input, processes it using Ollama's Llama2-Uncensored model, and generates responses in both text and speech, using a custom voice clone of Scarlett Johansson. The assistant functions entirely offline, ensuring privacy and customization.
Features

    Locally Hosted LLM: Runs on a local API using the llama2-uncensored model.
    Voice Cloning: Uses a custom voice sample (scarlet.mp3) for personalized responses.
    Three Modes:
        Continuous Listening: Always-on voice interaction.
        Single Response: One-time input from the console.
        Text-to-Speech: Converts typed text to spoken audio.
    Multilingual Support: Speech generation in multiple languages.

Prerequisites
System Requirements

    OS: Ubuntu Server or Desktop (or any Linux distro supporting Python 3).
    Hardware:
        GPU (for optimal performance): NVIDIA CUDA-enabled GPU.
        CPU: Supported but less efficient.

Dependencies

    Python: 3.8 or later
    Packages:

    pip install requests speechrecognition torch playsound TTS pyttsx3

        requests: For API communication.
        SpeechRecognition: Handles voice input.
        Torch: Executes machine learning models.
        Playsound: Plays the generated audio.
        TTS (Coqui): Converts text to speech.
        Pyttsx3: Alternative text-to-speech engine.

Installation

    Clone the Repository:

git clone https://github.com/username/EVA.git
cd EVA

Set Up Virtual Environment (Optional but recommended):

python3 -m venv venv
source venv/bin/activate

Install Dependencies:

    pip install -r requirements.txt

    Configure the LLM API:
        Ensure your LLM API is running locally at http://localhost:11434. If you're using Ollama, refer to their documentation for setup.

Usage
Command-Line Options:

    Continuous Listening:

python main.py

Single Response Mode:

python main.py -s

Text-to-Speech Mode:

    python main.py -a

Configuration
Changing the LLM Model:

    Edit llama_request.py:

    MODEL = "llama2-uncensored"  # Change to your desired model

Customizing the Voice:

    Replace scarlet.mp3 in text_to_speech.py with your own .mp3 file:

    SAMPLE_AUDIOS = "custom_voice.mp3"

Troubleshooting

    Speech Recognition Issues:
        Ensure your microphone is configured correctly.
        Adjust noise sensitivity using r.adjust_for_ambient_noise().

    Audio Playback Issues:
        Verify that the playsound library can access audio output.
        Ensure speech.wav is being generated.
