# Script to SRT Subtitle and Translator

This project helps you convert a script into subtitles and translate them into different languages.

### 1. **1-txt2srt.py** - Turn Your Script into Subtitles
- Provide a `.txt` file with your script.
- It converts the script into an `.srt` subtitle file with proper timing.

### 2. **2-translate-srt.py** - Translate Your Subtitles
- Use this to translate an `.srt` file into your desired language.

## How to Use
1. **Convert Script to Subtitles**:  
   Run `1-txt2srt.py`, select your `.txt` file, and generate the `.srt` file.
2. **Translate Subtitles**:  
   Run `2-translate-srt.py`, select your `.srt` file, choose a language, and get the translated subtitles.

## Requirements
- Python 3.x
- `googletrans` library (for translation)

## Installation
1. Clone or download the project.
2. Install the required library:
   ```bash
   pip install googletrans==4.0.0-rc1
   ```
