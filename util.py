import os

def get_text_or_file_path(input):
    if os.path.isfile(input):
        with open(input, 'r') as file:
            return file.read().split('\n\n')
    else:
        return [input]
    
def get_unique_folder_name(base_name):
    counter = 1
    while True:
        folder_name = f"{base_name}_{counter}"
        if not os.path.exists(folder_name):
            return folder_name
        counter += 1

def find_voice(voices, selected_voice):
    for voice in voices:
        if voice.name == selected_voice or voice.voice_id == selected_voice:
            return voice
    return None
