"""
Face and Eye Detection for Glasses
Works reliably on M4 Mac without MediaPipe
"""

import cv2
import numpy as np
from pathlib import Path

def detect_faces_and_eyes_with_glasses(image_path, output_path=None):
    """
    Detect faces and eyes using multiple Haar Cascade classifiers
    including specialized classifier for eyes behind glasses
    """
    # Read the image
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None
    
    # Create a copy for drawing
    result = img.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load eye cascades
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # Load eyeglasses cascade (specialized for glasses)
    eyeglasses_cascade_path = Path(__file__).parent / 'haarcascade_eye_tree_eyeglasses.xml'
    eyeglasses_cascade = cv2.CascadeClassifier(str(eyeglasses_cascade_path))
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    print(f"Found {len(faces)} face(s)")
    
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(result, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Region of interest for eyes (upper half of face)
        roi_gray = gray[y:y+int(h*0.6), x:x+w]
        roi_color = result[y:y+int(h*0.6), x:x+w]
        
        # Try standard eye detection first
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20)
        )
        
        # If standard detection finds few eyes, try eyeglasses cascade
        if len(eyes) < 2:
            eyes_glasses = eyeglasses_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=3,
                minSize=(20, 20)
            )
            
            # Use eyeglasses detection if it finds more eyes
            if len(eyes_glasses) >= len(eyes):
                eyes = eyes_glasses
                print(f"  Using eyeglasses cascade (found {len(eyes)} eyes)")
        else:
            print(f"  Using standard cascade (found {len(eyes)} eyes)")
        
        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(roi_color, 'Eye', (ex, ey-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    # Save or display result
    if output_path:
        cv2.imwrite(str(output_path), result)
        print(f"\nSaved result to: {output_path}")
    
    return result


if __name__ == "__main__":
    # Test with the photo
    img_path = Path(__file__).parent / "my_photo_assignemnt4.jpeg"
    output_path = Path(__file__).parent / "my_photo_detected.jpg"
    
    result = detect_faces_and_eyes_with_glasses(img_path, output_path)
    
    if result is not None:
        print("\n✓ Detection complete!")
