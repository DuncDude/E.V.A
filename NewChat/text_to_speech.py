from TTS.api import TTS
import torch
import os
from playsound import playsound

SAMPLE_AUDIOS = "scarlet.mp3"
OUTPUT_PATH = "./speech.wav"

def text_to_speech(llama_response):
    #Get device
    device="cuda:0" if torch.cuda.is_available() else "cpu"

    
    #TEXT = "My name is scarlet johansson, and I think you are beautiful, I think you are kind, and, I think you are great Duncan."

    print("Init model")
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to(device)
    print("Running text to speech conversion")
    #Run TTS
    tts.tts_to_file(llama_response,
                speaker_wav=SAMPLE_AUDIOS,
                language="en",  # "es" if the text is in spanish
                file_path=OUTPUT_PATH,
                split_sentences=True
                )
    print("All done!")

 
# for playing note.wav file
    print(f"Playing wav file: {OUTPUT_PATH}")
    playsound(OUTPUT_PATH)
    return
    
# #Listen to the generated audio
# import IPython
# IPython.display.Audio(OUTPUT_PATH)