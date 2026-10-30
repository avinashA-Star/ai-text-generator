# AI Text Generator

A simple project that uses a pre-trained GPT-2 model (Hugging Face) to continue any prompt you type.

## Setup
1. Install Python 3.8 or newer
2. Install dependencies:  pip install -r requirements.txt

## Run
python ai_text_generator.py

Type a prompt (e.g. "The future of technology is"), choose a max length, and the model continues your text. Type "quit" to exit.

## Notes
- The first run downloads the GPT-2 model (about 500 MB).
- Change "gpt2" to "distilgpt2" in load_generator() for a faster, smaller model.
- Raise temperature for more creative output, lower it for more focused text.
