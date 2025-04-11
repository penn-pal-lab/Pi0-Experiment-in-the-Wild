# comppress all videos in the static/videos/ folder
# if they are larger than 10MB, compress them to lower than 10MB
# if they are smaller than 10MB, do nothing

import os
import subprocess
import sys

def get_file_size_mb(file_path):
    """Get file size in megabytes"""
    return os.path.getsize(file_path) / (1024 * 1024)

def compress_video(input_path, output_path, target_size_mb=10):
    """Compress video to target size in MB"""
    try:
        # Get input video duration in seconds using ffprobe
        duration_cmd = [
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', input_path
        ]
        duration = float(subprocess.check_output(duration_cmd).decode().strip())
        
        # Calculate target bitrate (90% of target size to be safe)
        target_size = target_size_mb * 8192  # Convert MB to kilobits
        bitrate = int((target_size * 0.9) / duration)
        
        # Compress video using ffmpeg - use h264_nvenc (NVIDIA encoder) or if that fails, try other encoders
        # Try different encoders in order of preference
        encoders_to_try = ['h264_nvenc', 'h264_amf', 'h264_qsv', 'h264_mf', 'mpeg4']
        
        for encoder in encoders_to_try:
            compress_cmd = [
                'ffmpeg', '-i', input_path, '-y',  # -y to overwrite output file
                '-c:v', encoder, '-b:v', f'{bitrate}k',
                '-c:a', 'aac', '-b:a', '128k',
                output_path
            ]
            print(f"Trying encoder: {encoder}")
            print(f"Running command: {' '.join(compress_cmd)}")
            result = subprocess.run(compress_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if result.returncode == 0:
                print(f"Successfully compressed with {encoder}")
                return True
            else:
                print(f"Failed with encoder {encoder}: {result.stderr.decode()[:200]}...")
        
        # If all above encoders failed, try a simple copy with bitrate limit
        compress_cmd = [
            'ffmpeg', '-i', input_path, '-y',
            '-c:v', 'copy', '-b:v', f'{bitrate}k',
            '-c:a', 'copy',
            output_path
        ]
        print("Trying simple copy with bitrate limit")
        print(f"Running command: {' '.join(compress_cmd)}")
        result = subprocess.run(compress_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode != 0:
            print(f"All compression methods failed: {result.stderr.decode()[:200]}...")
            return False
        return True
    except Exception as e:
        print(f"Error during compression: {str(e)}")
        return False

def main():
    videos_dir = 'static/videos/success'
    size_threshold_mb = 10
    
    # Check if ffmpeg is installed
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in the PATH. Please install ffmpeg.")
        return
        
    # Create videos directory if it doesn't exist
    os.makedirs(videos_dir, exist_ok=True)
    
    # Process all video files in directory
    videos_found = False
    for filename in os.listdir(videos_dir):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            videos_found = True
            file_path = os.path.join(videos_dir, filename)
            file_size = get_file_size_mb(file_path)
            
            if file_size > size_threshold_mb:
                print(f"Compressing {filename} ({file_size:.2f}MB)")
                output_path = os.path.join(videos_dir, f'compressed_{filename}')
                success = compress_video(file_path, output_path)
                
                # Replace original with compressed if compression was successful
                if success and os.path.exists(output_path):
                    compressed_size = get_file_size_mb(output_path)
                    if compressed_size < file_size:
                        os.replace(output_path, file_path)
                        print(f"Compressed to {compressed_size:.2f}MB")
                    else:
                        os.remove(output_path)
                        print("Compression did not reduce file size, keeping original")
            else:
                print(f"Skipping {filename} ({file_size:.2f}MB) - already under threshold")
    
    if not videos_found:
        print(f"No video files found in {videos_dir}")

if __name__ == '__main__':
    main()
