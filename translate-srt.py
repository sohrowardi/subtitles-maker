import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from googletrans import Translator

def translate_srt(input_file, output_language):
    # Initialize translator
    translator = Translator()
    
    # Open and read the original SRT file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    current_index = 0
    
    # Mapping of languages
    language_map = {
        "1": "en",  # English
        "2": "bn",  # Bengali (moved to second)
        "3": "es",  # Spanish
        "4": "fr",  # French
        "5": "de",  # German
        "6": "it",  # Italian
        "7": "ja",  # Japanese
        "8": "ko",  # Korean
        "9": "zh-cn",  # Chinese (Simplified)
        "10": "hi",  # Hindi
        "11": "ar",  # Arabic
    }
    
    # Determine the target language code
    target_language = language_map.get(output_language)
    if not target_language:
        print("Invalid language selection.")
        return
    
    # Process the SRT file, translate content
    print(f"Translating file: {input_file}")
    
    # Iterate through the lines in the SRT file
    for line in lines:
        # Check if the line contains subtitles and is not a timestamp
        if '-->' in line or line.strip().isdigit():
            translated_lines.append(line)
        else:
            # Print what is being translated in real-time
            print(f"Translating: {line.strip()}")
            try:
                # Translate the line and append to the new list
                translated_text = translator.translate(line.strip(), src='auto', dest=target_language).text
                translated_lines.append(translated_text + '\n')
            except Exception as e:
                print(f"Error translating: {line.strip()}")
                translated_lines.append(line)
    
    # Output the new file name based on the selected language
    output_file = os.path.splitext(input_file)[0] + f'-{target_language}.srt'
    
    # Save the translated file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)
    
    print(f"Translation complete. File saved as: {output_file}")
    messagebox.showinfo("Success", f"File translated and saved as: {output_file}")

def select_file_and_language():
    # Set up the GUI
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Ask user to select the SRT file
    file_path = filedialog.askopenfilename(filetypes=[("SRT Files", "*.srt")])
    if not file_path:
        return

    # Ask user to select the language
    language_selection = simpledialog.askstring("Select Language", 
        "Select language:\n"
        "1. English\n"
        "2. Bengali\n"  # Bengali is now second
        "3. Spanish\n"
        "4. French\n"
        "5. German\n"
        "6. Italian\n"
        "7. Japanese\n"
        "8. Korean\n"
        "9. Chinese (Simplified)\n"
        "10. Hindi\n"
        "11. Arabic\n"
    )
    
    if not language_selection:
        return
    
    # Call the translation function
    translate_srt(file_path, language_selection)

# Run the program
if __name__ == "__main__":
    select_file_and_language()
