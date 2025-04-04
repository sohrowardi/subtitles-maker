# Script to SRT Subtitle and Translator

This project helps you convert a script into subtitles and translate them into different languages.

### 1. **txt2srt.py** - Turn Your Script into Subtitles
- You give it a `.txt` file with your script.
- It turns the script into an `.srt` subtitle file with timing.

### 2. **translate-srt.py** - Translate Your Subtitles
- After you make changes to the `.srt` file, run this.
- It will translate the subtitles into any language you choose.

## How to Use
1. **Convert Script to Subtitles**: Run `txt2srt.py`, choose your `.txt` file, and get the `.srt` file.
2. **Translate Subtitles**: Run `translate-srt.py`, choose your `.srt` file, pick a language, and get the translated subtitles.

## Requirements
- Python 3.x
- `googletrans` library (for translation)

## Installation
1. Download or clone the project.
2. Install the required library:
`pip install googletrans==4.0.0-rc1`
