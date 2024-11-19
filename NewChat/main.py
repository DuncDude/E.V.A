import sys


from speech_to_text_google import listen
from llama_request import send_prompt_get_response
from text_to_speech import text_to_speech

def constant_listening():
    print("Activating constant listening")
    while(True):
        prompt =  listen()
        llama_response = send_prompt_get_response(prompt)
        text_to_speech(llama_response)

def single_response():
    print("Activating single response")
    prompt = input("Ask me anything:")
    llama_response = send_prompt_get_response(prompt)
    text_to_speech(llama_response)

def simple_audio_gen():
    print("Activating text to speech")
    prompt = input("Text to speech:")
    text_to_speech(prompt)

if "-s" in sys.argv:
    single_response()
elif "-a" in sys.argv:
    simple_audio_gen()
else:  
    constant_listening()