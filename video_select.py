import cv2
import os

def extract_left_view(input_path):
    # Get directory and filename
    dir_path = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    
    # Create output path with modified filename
    base_name = os.path.splitext(filename)[0]
    output_path = os.path.join(dir_path, f"{base_name}_left.mp4")
    
    # Open the video file
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Create VideoWriter for output
    left_width = width // 2  # Assuming the video is split exactly in half
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (left_width, height))
    
    # Process frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Extract left half
        left_frame = frame[:, :left_width]
        
        # Write to output file
        out.write(left_frame)
    
    # Release resources
    cap.release()
    out.release()
    
    print(f"Left view extracted and saved to: {output_path}")

if __name__ == "__main__":
    input_video = r"static\videos\failure\right_pick_up_the_pokeball_and_put_it_in_the_bowl.mp4"
    extract_left_view(input_video)

# get left piece of the video
