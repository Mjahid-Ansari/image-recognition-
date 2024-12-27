import boto3
import os

def detect_labels(image_path):
    # Initialize the Rekognition client without hardcoding credentials
    client = boto3.client('rekognition', region_name='ap-south-1')

    try:
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        response = client.detect_labels(Image={'Bytes': image_bytes})
        return response['Labels']
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

def main():
    image_path = 'vimal.jpg'
    
    # Ensure the image exists
    if not os.path.exists(image_path):
        print(f"Image {image_path} not found.")
        return
    
    labels = detect_labels(image_path)
    
    if labels:
        print("Labels in the image:")
        for label in labels:
            print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")
    else:
        print("No labels detected.")

if __name__ == "__main__":
    main()
