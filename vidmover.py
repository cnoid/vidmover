import os
import sys
from moviepy.editor import VideoFileClip
from shutil import move

def filter_and_move_videos(source_dir, dest_dir, min_duration):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                clip = VideoFileClip(filepath)
                if clip.duration < min_duration:
                    print(f"Moving file below duration threshold: {filepath}")
                    move(filepath, os.path.join(dest_dir, filename))
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py path/to/source path/to/destination DurationInSeconds")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    min_duration = int(sys.argv[3])  # Duration in seconds

    filter_and_move_videos(source_dir, dest_dir, min_duration)
