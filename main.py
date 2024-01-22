import os
import argparse
import util
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate, play, voices, save, VoiceSettings
from pydub import AudioSegment

load_dotenv()
elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')

if elevenlabs_api_key is None:
    raise Exception('ElevenLabs API Key not found. Please set the environment variable ELEVENLABS_API_KEY.')

set_api_key(elevenlabs_api_key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate voice from text or file.')
    parser.add_argument('input', type=str, nargs='?', help='Text or path to the text file.')
    parser.add_argument('--list-voices', action='store_true', help='List all available voices and exit.')
    parser.add_argument('--voice', type=str, help='Select voice by name or ID.')
    parser.add_argument('--play-voice', action='store_true', help='Play the generated voice if set.')
    parser.add_argument('--voice-stability', type=float, help='Set voice stability.')
    parser.add_argument('--voice-similarity', type=float, help='Set voice similarity.')
    parser.add_argument('--voice-style', type=float, help='Set voice style.')
    parser.add_argument('--voice-boost', type=bool, help='Set voice boost.')

    args = parser.parse_args()

    selected_voice = args.voice if args.voice else os.getenv('SELECTED_VOICE')
    voice_stability = args.voice_stability if args.voice_stability else float(os.getenv('VOICE_STABILITY', '0.5'))
    voice_similarity = args.voice_similarity if args.voice_similarity else float(os.getenv('VOICE_SIMILARITY', '0.75'))
    voice_style = args.voice_style if args.voice_style else float(os.getenv('VOICE_STYLE', '0.0'))
    voice_boost = args.voice_boost if args.voice_boost else bool(os.getenv('VOICE_BOOST', 'True'))

    if args.list_voices:
        voices = voices()
        for voice in voices:
            print(f"Name: \"{voice.name}\"\nVoice ID: \"{voice.voice_id}\"\n")
    elif args.input is not None:
        paragraphs = util.get_text_or_file_path(args.input)
        voices = voices()
        voice = util.find_voice(voices, selected_voice)
        if voice is None:
            raise Exception(f'No voice found with name or ID "{selected_voice}".')
        voice.settings = VoiceSettings(stability=voice_stability, similarity_boost=voice_similarity, style=voice_style, use_speaker_boost=voice_boost)
        print(f"Selected voice: \"{voice.name}\"")
        folder_name = util.get_unique_folder_name(voice.name)
        os.makedirs(folder_name)
        counter = 1
        for paragraph in paragraphs:
            print(f"Generating voice for text: \"{paragraph}\"")
            audio = generate(text=paragraph, voice=voice.voice_id, model="eleven_multilingual_v2")
            if args.play_voice:
                play(audio)
            filename = f"{folder_name}/{voice.name}_{counter}.mp3"
            save(audio, filename)
            counter += 1
        if len(paragraphs) > 1:
            combined = AudioSegment.empty()
            for i in range(1, counter):
                filename = f"{folder_name}/{voice.name}_{i}.mp3"
                combined += AudioSegment.from_mp3(filename)
            combined.export(f"{folder_name}/{voice.name}_final.mp3", format='mp3')
    else:
        parser.error("the following arguments are required: input")
