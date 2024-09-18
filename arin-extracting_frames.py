import cv2
import os
import random

def extract_random_frames(video_path, output_folder, video_name, num_frames=32):
    """Extract 16 continuous frames from a random location in the video."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)
    
    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Ensure we can extract 16 frames
    if total_frames < num_frames:
        print(f"Video {video_path} does not have enough frames.")
        return

    # Set the video capture to the starting frame

    # Extract and save the frames
    rand_frames = random.sample(range(total_frames), num_frames)
    for i in range(num_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, rand_frames[i])
        ret, frame = cap.read()
        if not ret:
            break  # Exit if there are no more frames

        # Save the frame as an image
        # frame_filename = os.path.join(output_folder, f"{video_name}_{start_frame + i:04d}.jpg")
        frame_filename = os.path.join(output_folder, f"{video_name}-{i}.jpg")
        cv2.imwrite(frame_filename, frame)

    cap.release()  # Release the video capture object
    print(f"Extracted {num_frames} frames from {video_path}.")


    # Randomly select a starting frame
    # start_frame = random.randint(0, total_frames - num_frames)
    # # Set the video capture to the starting frame
    # cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # # Extract and save the frames
    # for i in range(num_frames):
    #     ret, frame = cap.read()
    #     if not ret:
    #         break  # Exit if there are no more frames

    #     # Save the frame as an image
    #     # frame_filename = os.path.join(output_folder, f"{video_name}_{start_frame + i:04d}.jpg")
    #     frame_filename = os.path.join(output_folder, f"{video_name}-{i}.jpg")
    #     cv2.imwrite(frame_filename, frame)

    # cap.release()  # Release the video capture object
    # print(f"Extracted {num_frames} frames from {video_path} starting at frame {start_frame}.")

def process_videos_in_folder(video_folder, output_base_folder):
    """Process all videos in the specified folder."""
    # List all video files in the folder
    for filename in os.listdir(video_folder):
        if filename.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(video_folder, filename)
            # output_folder = os.path.join(output_base_folder, os.path.splitext(filename)[0])  # Create a unique output folder for each video
            output_folder = output_base_folder
            extract_random_frames(video_path, output_folder, filename.split('.')[0])

# video_folder = "../Celeb-DF/Celeb-real"
video_folder = "../Celeb-DF/Celeb-synthesis"
output_base_folder = "celeb_dataset" 
process_videos_in_folder(video_folder, output_base_folder)