import os
import subprocess

def convert_mov_to_mp4(folder_path):
    # Get all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if file is .mov
            if file.lower().endswith('.mov'):
                input_path = os.path.join(root, file)
                # Create output path with .mp4 extension
                output_path = os.path.join(root, os.path.splitext(file)[0] + '.mp4')
                
                # Use ffmpeg to convert
                try:
                    subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'copy', '-c:a', 'copy', output_path], check=True)
                    print(f"Successfully converted {file} to MP4")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {file}: {e}")

if __name__ == "__main__":
    # Get current directory if no path specified
    folder_path = os.getcwd()
    convert_mov_to_mp4(folder_path)