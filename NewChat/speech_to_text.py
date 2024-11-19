# Python program to translate
# speech to text

import speech_recognition as sr
from llama_request import send_prompt_get_response

# Initialize the recognizer 
r = sr.Recognizer()

# Loop infinitely for user to speak
while True:
    try:
        # Use the microphone as source for input.
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # Listens for the user's input 
            print("listening")
            audio2 = r.listen(source2)
            
            # Using Sphinx to recognize audio
            MyText = r.recognize_sphinx(audio2)
            MyText = MyText.lower()
            print(f"Did you say {MyText}")
            
            # Assuming send_prompt_get_response() function sends the recognized text 
            # to some service and prints the response
            send_prompt_get_response(MyText)     
    except sr.RequestError as e:
        print(f"Could not request results from Sphinx service; {e}")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")