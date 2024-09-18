import os
import shutil

def select_videos(videos_folder, folders_of_interest, output_folder):
    """
    Selects videos from a source folder based on the folder names in another directory.

    Args:
        videos_folder (str): Path to the folder containing all videos.
        folders_of_interest (str): Path to the folder containing subfolders named after videos.
        output_folder (str): Path to the folder where the selected videos will be copied.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of folder names in the folders_of_interest
    subfolder_names = set(os.listdir(folders_of_interest))

    # Loop through all videos in the videos folder
    for video_file in os.listdir(videos_folder):
        video_name, video_ext = os.path.splitext(video_file)
        
        # Check if the video name matches any folder name in the folders_of_interest
        if video_name in subfolder_names:
            source_path = os.path.join(videos_folder, video_file)
            destination_path = os.path.join(output_folder, video_file)
            
            # Copy the video to the output folder
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {video_file}")

if __name__ == "__main__":
    videos_folder = "mix"  # Replace with the path to the folder containing 1000 videos
    folders_of_interest = "mix/frames"  # Replace with the path to the folder containing 100 subfolders
    output_folder = "mix/test_samples"  # Replace with the path where you want to save the selected videos
    
    select_videos(videos_folder, folders_of_interest, output_folder)
