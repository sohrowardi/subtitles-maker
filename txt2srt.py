import datetime
import os
from tkinter import Tk, filedialog

def format_timecode(seconds):
    td = datetime.timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def txt_to_srt(input_file, duration=3):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    folder = os.path.dirname(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(folder, f"{base_name}.srt")

    with open(output_file, 'w', encoding='utf-8') as f:
        start_time = 0
        for index, line in enumerate(lines, start=1):
            end_time = start_time + duration
            f.write(f"{index}\n")
            f.write(f"{format_timecode(start_time)} --> {format_timecode(end_time)}\n")
            f.write(f"{line}\n\n")
            start_time = end_time

    print(f"✅ SRT file created at: {output_file}")

def main():
    root = Tk()
    root.withdraw()  # Hide the main window
    txt_path = filedialog.askopenfilename(
        title="Select a .txt file",
        filetypes=[("Text files", "*.txt")]
    )
    if txt_path:
        txt_to_srt(txt_path)
    else:
        print("❌ No file selected.")

if __name__ == "__main__":
    main()