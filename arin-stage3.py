import json
import torch
from sklearn.cluster import KMeans
from data.transform import get_transforms
from model import ECL
from PIL import Image
import os

def load_model(model_path):
    """Load the trained model from the specified path."""
    model = ECL()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def classify_videos(video_paths, model):
    """Classify videos as real or fake based on extracted features."""
    features = []
    transform = get_transforms(name="val")
    
    # Extract features from each video
    # MAKE A FUNTION TO EXTRACT FRAMES FROM VIDEO HERE
    for video_path in video_paths:
        feature_vector = extract_features(video_path, model)
        features.append(feature_vector)

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=2)
    labels = kmeans.fit_predict(features)

    # Calculate inter-frame correlation and classify
    for label in set(labels):
        cluster_features = [features[i] for i in range(len(features)) if labels[i] == label]
        avg_correlation = calculate_avg_correlation(cluster_features)
        classification = "Real" if avg_correlation < threshold else "Fake"  # Define a threshold
        print(f"Cluster {label}: Average Correlation = {avg_correlation}, Classification: {classification}")

def calculate_avg_correlation(cluster_features):
    """Calculate the average correlation of features in a cluster."""
    # Implement correlation calculation logic here
    # For example, you could use numpy to compute pairwise correlations
    import numpy as np
    correlation_matrix = np.corrcoef(cluster_features)
    avg_correlation = np.mean(correlation_matrix)
    return avg_correlation

if __name__ == "__main__":
    # Load the trained model
    model = load_model("save/SupCon/_models/2024-09-02 23-23-36/last.pth")
    
    # List of video paths to classify
    video_paths = ["mix/frames-singles/id0_0000-4.jpg", "mix/frames-singles/id10_0000-0.jpg"]
    
    # Define a threshold for classification
    threshold = 0.5  # Adjust based on your needs

    # Classify the videos
    classify_videos(video_paths, model)