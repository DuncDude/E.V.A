import requests
import json
from text_to_speech import text_to_speech

MODEL = "llama2-uncensored"

def send_prompt_get_response(prompt_text):
    print(f"Sending prompt to llama model: {MODEL}")
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "prompt": prompt_text
    }
    
    full_response_text = ""
    done = False

    response = requests.post(url, json=payload, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Process each line in the response text
        for line in response.text.splitlines():
            try:
                # Attempt to decode each line as JSON
                response_data = json.loads(line)
                full_response_text += response_data.get("response", "")
                done = response_data.get("done", False)
                if done:
                    break
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
                break
    else:
        print(f"Failed to get response: {response.status_code}")
    print(f"Generated text: {full_response_text}")
    return full_response_text
