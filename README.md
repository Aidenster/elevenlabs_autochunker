# ElevenLabs Autochunker

This project is a Python application that uses the ElevenLabs API to generate voice from text or a text file.

## Installation

1. Clone this repository.
2. Install the required Python packages by running `pip install -r requirements.txt`.

## Configuration

Copy the `.env.template` file to a new file named `.env` and fill in the following environment variables:

- `ELEVENLABS_API_KEY`: Your ElevenLabs API key.
- `SELECTED_VOICE`: The name or ID of the voice to use.
- `VOICE_STABILITY`: The stability of the voice (default is 0.35).
- `VOICE_SIMILARITY`: The similarity of the voice (default is 0.75).
- `VOICE_STYLE`: The style of the voice (default is 0.0).
- `VOICE_BOOST`: Whether to boost the voice (default is True).

## Usage

Run the `main.py` script with the following command-line arguments:

- `input`: The text or path to the text file to generate voice from.
- `--list-voices`: List all available voices and exit.
- `--voice`: Select voice by name or ID.
- `--play-voice`: Play the generated voice.
- `--voice-stability`: Set voice stability.
- `--voice-similarity`: Set voice similarity.
- `--voice-style`: Set voice style.
- `--voice-boost`: Set voice boost.

Example:

```sh
python main.py "Hello, world!" --voice "John Doe" --play-voice
```
